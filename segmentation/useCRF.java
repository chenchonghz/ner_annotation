import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class useCRF {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		File dir = new File(".");
		String targetName = "A 00 (1).txt";
		
		String modelFile = dir.getCanonicalPath() + File.separator + "data" + File.separator + "train" + File.separator + "model" + File.separator + "model";
		String input = dir.getCanonicalPath() + File.separator + "data" + File.separator + "process" + File.separator + "input";
		String output = dir.getCanonicalPath() + File.separator + "data" + File.separator + "process" + File.separator + "output";
		process(modelFile,targetName,input,output);
	}
	
	public static void process(String modelName, String targetName,String input, String output) throws IOException{
		System.out.println("train");
		File dir = new File(".");
		Process process = new ProcessBuilder(dir.getAbsolutePath() + File.separator + "crf_test.exe","-m",modelName,input + File.separator + targetName).start();
		InputStream is = process.getInputStream();
		InputStreamReader isr = new InputStreamReader(is);
		BufferedReader br = new BufferedReader(isr);
		String line;

		System.out.printf("Output of running is:");
		dir = new File(output);
		if(!dir.exists()){
			dir.mkdir();
		}
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(output + File.separator + targetName),"UTF-8"));
		while ((line = br.readLine()) != null) {
		  //System.out.println(line);
			bw.write(line);
			bw.newLine();
		}
		br.close();
		bw.close();
		System.out.println("finished");
	}
	
	
	public static void processAll(String modelName, String[] targetNames,String input, String output) throws IOException{
		for (String tar: targetNames){
			File dir = new File(input + File.separator + tar);
			if(!dir.exists()){
				System.err.println( dir.getAbsolutePath() + " does not exist!");
				continue;
			}
			process(modelName,tar,input,output);
		}
	}
}
