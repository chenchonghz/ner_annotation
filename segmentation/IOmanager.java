import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.util.HashSet;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class IOmanager {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static Set<String> loadDict(String dictPath) throws IOException, FileNotFoundException{
		final String segSign = " ";
		Set<String> dictSet = new HashSet<String>();
		int count = 0;
		BufferedReader dict = new BufferedReader(new InputStreamReader(new FileInputStream(new File(dictPath)), "UTF-8"));
		String line;
		while ((line = dict.readLine()) != null) {
			String [] oneLine = line.split(segSign);
			for(String a : oneLine){
				if(dictSet.add(a)){
					count++;
				}
			}
		}
		dict.close();
		System.out.println("load " + count + " word(s)");
		return dictSet;
	}
	
	public static String [] getTargetNames(int start, int end){
		if(start > end)
			return null;
		String [] targetNames = new String [end - start + 1];
		for(int i = 0; i <= end - start; i++){
			//targetNames[i] = "A 00 (" + (i + start) + ").txt";
			targetNames[i] = (i + start) + ".txt";
		}
		return targetNames;
	}
	
	public static String[] getRandNames(int index) throws Exception, FileNotFoundException{
		File dir = new File(".");
		String inputPath = dir.getCanonicalPath() + File.separator + "data" + File.separator + "splits" + File.separator + "rand" + index +File.separator+ "ranList" + index + ".txt";
		File cur = new File(inputPath);
		System.out.println("get files from " + inputPath);
		if(!cur.exists())
			return null;
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(cur), "UTF-8"));
		String targetName;
		HashSet<String> targetNames = new HashSet<String>();
		while((targetName = br.readLine()) != null){
			targetNames.add(targetName);
		}
		br.close();
		return (String[])targetNames.toArray(new String[targetNames.size()]);
	}
	
	public static int checkRight(String[] right, String path, String targetName, BufferedWriter bw) throws Exception, FileNotFoundException{
		int number = 0;
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(new File(path + File.separator + targetName)), "UTF-8"));
		String line = null;
		while((line = br.readLine())!=null){
			for(String rightWord : right){
				Pattern pattern1 = Pattern.compile(rightWord);
				Matcher matcher = pattern1.matcher(line);
				while (matcher.find()) {
					bw.write(String.format("Found the text \"%s\" starting at index %d and ending at index %d.", matcher.group(), matcher.start(), matcher.end()));
					bw.newLine();
					number++;
				}
			}
		}
		br.close();
		return number;
	}
	
	public static void mergeFile(String input, String output, String[] set) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(output),"UTF-8"));
		
		for(String trainFile : set){
			File dir = new File(input + File.separator + trainFile);
			if(!dir.exists()){
				System.err.println(dir.getAbsolutePath() + " does not exist!");
				continue;
			}
			BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(new File(input + File.separator + trainFile)), "UTF-8"));
			String line;
			while((line = br.readLine()) != null){
				bw.write(line);
				bw.newLine();
			}
			br.close();
		}
		bw.close();
	}
}
