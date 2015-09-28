import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class postProcessOutput {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		System.out.println("过敏\u0020病史");
		
		File dir = new File(".");
		String toolName = "stfdnlp";
		String dictName = "generalchinesewords";
		String input =  dir.getCanonicalPath() + File.separator + "data" + File.separator + "result" + File.separator + toolName + File.separator + "cross" + File.separator + "final" + File.separator + dictName;
		//String input =  dir.getCanonicalPath() + File.separator + "data" + File.separator + "result" + File.separator + toolName + File.separator + "cross" + File.separator + "final" + File.separator + dictName;
		String output = dir.getCanonicalPath() + File.separator + "data" + File.separator + "result" + File.separator + "posttool" + File.separator + "cross" + File.separator + "final" + File.separator + dictName;
		String[] targetNames = IOmanager.getRandNames(4);
		//String[] targetNames = {"test.txt"};
		BufferedWriter debug = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(output + File.separator + "debug.txt")),"UTF-8"));
		for(int i = 0; i < args.length; i++){
			if(updateFromArgs(i,"toolName",args)) toolName = args[i+1];
			if(updateFromArgs(i,"dictlName",args)) dictName = args[i+1];
			if(updateFromArgs(i,"input",args)) input = args[i+1];
			if(updateFromArgs(i,"output",args)) output = args[i+1];
			if(updateFromArgs(i,"targetNames",args)) targetNames = args[i+1].split(",");
		}
		System.out.println("total files " + targetNames.length);
		File out = new File(output);
		for(File temp : out.listFiles()){
			temp.delete();
		}
		
		//out.delete();
		for(String targetName: targetNames){
			//handleSpecial(targetName,input,output,debug);
			//handleSpecial(targetName,input,output,debug);
		}
		debug.close();
	}
	
	public static boolean updateFromArgs(int i, String target, String[] args){
		if(args[i].equals(target) && i < args.length - 1)
			return true;
		else
			return false;
	}

	public static void handleSpecial(String targetName, String input, String output,BufferedWriter debug) throws Exception, FileNotFoundException{
		System.out.println(input + File.separator + targetName);
		if(!new File(input + File.separator + targetName).exists()){
			System.err.println( targetName + " does not exist ! return");
			return;
		}
		File fout = new File(output);
		if(!fout.exists())
			fout.mkdirs();
		if(debug == null)
			debug = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(output + File.separator + "debug.txt")),"UTF-8"));
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(new File(input + File.separator + targetName)), "UTF-8"));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(output + File.separator + targetName)),"UTF-8"));

		debug.write("load " + input + File.separator + targetName);
		debug.newLine();
		String line = null;
		HashMap<String,String> pt = new HashMap<String,String>();
		
		//Pattern[] Patterns = new Pattern[1];
		
		pt.put("次\\s+/\\s+分","次/分");
		pt.put("(\\d+)/(\\d+\\s+mmHg)","$1 / $2");
		pt.put("mg\\s+/\\s+次","mg/次");
		pt.put("次\\s+/\\s+日","次/日");
		pt.put("次、日", "次/日");
		pt.put("B\\s+超", "B超");
		pt.put("X\\s+线", "X线");
		pt.put("过\\s+敏\\s+病\\s+史", "过敏\u0020病史");
		
		System.out.println(pt.keySet().size());
//		for(String s: pt.keySet()){
//			System.out.println(s);
//		}
		while((line = br.readLine())!=null){
			boolean needChange = false;
			debug.write(line);
			debug.newLine();
			for(String s: pt.keySet()){
//				debug.write("load " + s);
//				System.out.println(s);
//				debug.newLine();
				Pattern p = Pattern.compile(s);
				Matcher matcher1 = p.matcher(line);
				while (matcher1.find()) {
					debug.write(String.format("Found the text \"%s\" starting at index %d and ending at index %d.%n", matcher1.group(), matcher1.start(), matcher1.end()));
					debug.newLine();
					needChange = true;
				}
			}

			String newLine = line;
			if(needChange){
				for(String s: pt.keySet()){
					newLine = newLine.replaceAll(s, pt.get(s));
				}	
				debug.write("change it");
				debug.newLine();
				debug.write(newLine);
				debug.newLine();
			}
			bw.write(newLine.toString());
			bw.newLine();
		}
		br.close();
		bw.close();

	}

}
