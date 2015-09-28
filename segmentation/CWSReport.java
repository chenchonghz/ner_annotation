import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;


public class CWSReport {

	private String calPath;
	private String humanPath;
	Set<String> dict;

	int totalWords;
	int totalRightWords;
	int totalMatchWords;
	int totalWordsOOV;
	int totalMatchWordsOOV;
	int totalRightWordsOOV;
	
	float overAllF;

	public void initDict(String dictPath) throws FileNotFoundException, IOException{
		this.dict = IOmanager.loadDict(dictPath);
	}
		
	public void resetCount(){
		this.totalWords = 0;
		this.totalRightWords = 0;
		this.totalMatchWords = 0;
		this.totalWordsOOV = 0;
		this.totalMatchWordsOOV = 0;
		this.totalRightWordsOOV =0;
		this.overAllF = 0;
	}

	public void run(String debugFile) throws FileNotFoundException, IOException{
		File dir = new File(".");
		File debug = new File(debugFile);
		if(!debug.exists()){
			System.err.println("no debug file, choose default path");
			debug = new File(dir.getCanonicalPath() + File.separator + "data" + File.separator +"cross");
			if(!debug.exists()){
				debug.mkdir();
			}
		}
		debug =new File(debug.getCanonicalFile() + File.separator + "debug.txt");
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(debug),"UTF-8"));

		StringBuilder calSB = loadText(this.calPath);
		StringBuilder humanSB = loadText(this.humanPath);
		String calWord = null, humanWord = null;
		int calCount = 0, humanCount = 0;
		//		bw.write("The space is " + ' ' + " which binary value is " + Integer.toBinaryString((int)' ') + "\n");
		//		bw.write("The next line is " + '\n' + " which binary value is " + Integer.toBinaryString((int)'\n') + "\n");
		//		bw.write("The tab is " + '\t' + " which binary value is " + Integer.toBinaryString((int)'\t') + "\n");
		//		bw.write("The return is " + '\r' + " which binary value is " + Integer.toBinaryString((int)'\r') + "\n");

		while(humanSB.length() != 0 && calSB.length() != 0){
			if(calCount == humanCount){
				humanWord = getNextWord(humanSB,bw);
				calWord = getNextWord(calSB,bw);
				calCount += calWord.length();
				humanCount += humanWord.length();
				this.totalWords++;
				this.totalRightWords++;
				if(this.dict == null || !dict.contains(humanWord.toString())){
					this.totalRightWordsOOV++;
				}
				if(this.dict == null || !dict.contains(calWord.toString())){
					this.totalWordsOOV++;
				}
			}else if(calCount > humanCount){
				humanWord = getNextWord(humanSB,bw);
				humanCount += humanWord.length();
				this.totalRightWords++;
				if(this.dict == null || !this.dict.contains(humanWord.toString())){
					this.totalRightWordsOOV++;
				}
			}else{
				calWord = getNextWord(calSB,bw);
				calCount += calWord.length();
				this.totalWords++;
				if(this.dict == null || !dict.contains(calWord.toString())){
					this.totalWordsOOV++;
				}
			}
			//byte[] calB = calWord.getBytes("UTF-8");
			//byte[] humB = humanWord.getBytes("UTF-8");
			//bw.write("last cal word is " + calWord + " binaray value is " + calB.toString() + " last human word is " + humanWord + " binaray value is " + humB.toString());
			bw.write("last cal word is " + calWord + " last human word is " + humanWord);
			bw.write(" last cal word is " + calCount + "\t last human word is " + humanCount + "\n");
			if(humanWord.equals(calWord)){
				this.totalMatchWords++;
				calCount = 0;
				humanCount = 0;	
				if(this.dict == null || !dict.contains(humanWord.toString())){
					this.totalMatchWordsOOV++;
				}
				bw.write("match " + humanWord.toString() + "\n");
			}
			//			if(!this.dict.contains(calWord.toString())){
			//				this.totalNewWords++;
			//			}
			//			if(!this.dict.contains(humanWord.toString()){
			//				this.totalNewWordsFromDict++;
			//			}

			//			totalWords;
			//			totalRightWords;
			//			totalMatchWords;
			//			int totalNewWords;
			//			int totalNewMatchWords;
			//			int totalNewWordsFromDict;
		}
		while(humanSB.length() != 0){
			humanWord = getNextWord(humanSB,bw);
			this.totalRightWords++;
			//System.out.println("humanWord is " + humanWord.toString());
			if(this.dict == null || !dict.contains(humanWord.toString())){
				this.totalRightWordsOOV++;
			}
		}
		while(calSB.length() != 0){
			calWord = getNextWord(calSB,bw);
			this.totalWords++;
			if(this.dict == null || !dict.contains(calWord.toString())){
				this.totalWordsOOV++;
			}
		}
		bw.close();
	}

	public static String getNextWord(StringBuilder text , BufferedWriter bw) throws IOException{
		StringBuilder nextWord = new StringBuilder();
		while((text.length() != 0) && isBreak(text.charAt(0))){
			//bw.write(text.charAt(0) + "\n");
			text.deleteCharAt(0);
		}
		while(text.length() != 0){
			if(isBreak(text.charAt(0))){
				while((text.length() != 0) && isBreak(text.charAt(0))){
					//bw.write(text.charAt(0) + "\n");
					text.deleteCharAt(0);
				}
				break;
			}else{
				//bw.write("The char is " + text.charAt(0) + " which binary value is " + Integer.toHexString((int)text.charAt(0)) + "\n");
				nextWord.append(text.charAt(0));
				text.deleteCharAt(0);
			}
		}
		return nextWord.toString();
	}

	public static boolean isBreak(char sign){
		return sign == '\n' || sign == '\t' || sign == '\r' || Character.isWhitespace(sign);
	}

	public static StringBuilder loadText(String Path) throws IOException, FileNotFoundException{
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(new File(Path)), "UTF-8"));
		StringBuilder sb = new StringBuilder();
		String line = br.readLine();
		while (line != null) {
			sb.append(line);
			sb.append("\n");
			line = br.readLine();
		}
		br.close();
		return sb;
	}

	public void setCalPath(String inPath){
		this.calPath = inPath;
	}

	public void setHumPath(String inPath){
		this.humanPath = inPath;
	}

	public String report(String dictPath){
		StringBuilder report = new StringBuilder ();
		report.append("# of words in " + dictPath + "\t is " + dict.size() + "\n");
		System.out.println(this.calPath);
		report.append("Overall : \n");
		System.out.println("Overall : ");
		report.append(this.singleReport(this.totalMatchWords, this.totalWords, this.totalRightWords, true));
		report.append("OOV : \n");
		System.out.println("OOV : ");
		report.append(this.singleReport(this.totalMatchWordsOOV, this.totalWordsOOV, this.totalRightWordsOOV));
		report.append("IV : \n");
		System.out.println("IV : ");
		report.append(this.singleReport(this.totalMatchWords - this.totalMatchWordsOOV, this.totalWords - this.totalWordsOOV, this.totalRightWords - this.totalRightWordsOOV));
		return report.toString();
	}

	private StringBuilder singleReport(int MatchWords, int Words, int RightWords){
		return this.singleReport(MatchWords, Words, RightWords, false);
	}
	private StringBuilder singleReport(int MatchWords, int Words, int RightWords, boolean allOver){
		float precison = (float) MatchWords/Words;
		float recall = (float) MatchWords/RightWords;
		float Fmesure = 2*precison*recall/(precison+recall);
		if(allOver)
			this.overAllF = Fmesure;
		//float error = (float) (Words - MatchWords)/RightWords;
		StringBuilder report = new StringBuilder ();
		report.append(" total Words is " + Words + "\t total Right words is " + RightWords + "\t total match words is " + MatchWords + "\n");
		report.append(" precison is " + precison + "\n");
		report.append(" recall is " + recall + "\n");
		report.append(" F-mesure is " + Fmesure + "\n");
		//report.append(" ER is  " + error + "\n");
		System.out.println(" total Words is " + Words + "\t total Right words is " + RightWords + "\t total match words is " + MatchWords);
		System.out.println(" precison is " + precison);
		System.out.println(" recall is " + recall);
		System.out.println(" F-mesure is " + Fmesure);
		//System.out.println(" ER is  " + error);
		return report;
	}

	public String process(String[] targetNames, String toolName, String dictPath, String toolResultPath, String humanResultPath, String debug) throws IOException{
		File dir = new File(".");
		String log = "";
		this.resetCount();
		//String dictPath = dir.getCanonicalPath() + File.separator + "data" + File.separator + "dict" + File.separator + "generalchinesewords.txt";
		this.initDict(dictPath);
		for(String targetName : targetNames){
			//String rawPath = dir.getCanonicalPath() + File.separator + "data" + File.separator + "raw" + File.separator + targetName;

			String calPath = toolResultPath + File.separator + targetName;
			//String postHumanPath = dir.getCanonicalPath() + File.separator + "data" + File.separator + "result" + File.separator + "posthuman" + File.separator + targetName;
			String postHumanPath = humanResultPath + File.separator + targetName;
			File fout = new File(postHumanPath);
			if(fout.exists()){
				//log = log + " load cal source " + calPath + "\n";
				//log = log + " load hum source " + postHumanPath + "\n";
				this.setCalPath(calPath);
				this.setHumPath(postHumanPath);
				this.run(debug);
			}
		}
		return log + this.report(dictPath);	
	}
	
	public float getOverAllF(){
		return this.overAllF;
	}


	public static void main(String[] args) throws Exception {

		// TODO Auto-generated method stub
		String[] targetNames = {"A 00 (16).txt"};//,"A 00 (2).txt","A 00 (3).txt"};
		//CWSReport.preProcess(targetNames);
		String[] dictNames = {"generalchinesewords","test7","generalchinesewords+test7"};
		//String[] dictNames = {"generalchinesewords"};

		Map<String, String[]> tools = new HashMap<String, String[]>();
		//tools.put("stfdnlp",new String[]{"pku","ctb"});
		tools.put("stfdnlp",dictNames);
		//tools.put("fdnlp",new String[]{"seg"});
		//tools.put("ictclas", new String[]{"default"});
		boolean appendFromPrevious = false;

		File dir = new File(".");
		File fout = new File(dir.getCanonicalPath() + File.separator + "data" + File.separator +"result" + File.separator + "summaryTest7.txt");
		BufferedWriter bw;

		if(appendFromPrevious){
			BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(fout), "UTF-8"));
			String line;
			StringBuilder last = new StringBuilder();
			while((line = br.readLine())!= null){
				last.append(line);
				last.append("\n");
			}
			br.close();
			bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(fout),"UTF-8"));
			last.append("\n");
			bw.write(last.toString());
		}else{
			bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(fout),"UTF-8"));
		}
		CWSReport rep = new CWSReport();
		for(String dictName : dictNames){
			for(String toolName : tools.keySet()){
				String[] modelNames = tools.get(toolName);
				for(String modelName : modelNames){
					String outputPath = dir.getCanonicalPath() + File.separator + "data" + File.separator + "result" + File.separator +"stfdnlp" + File.separator + "cross";
					bw.write("***************************************************************************************************\n");
					bw.write("\t Tools Name :" + toolName + "\t Dict Name : " + dictName + "\t Model Name :" + modelName + "\n");
					bw.write("***************************************************************************************************\n");
					//bw.write(rep.process(targetNames,toolName,dictName,modelName));	
					//bw.write(rep.process(targetNames,toolName,dictName,outputPath));
				}
			}
		}
		bw.close();
	}


}
