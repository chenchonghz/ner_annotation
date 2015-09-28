import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;

public class trainCRF {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		File dir = new File(".");
		String templateFile = dir.getCanonicalPath() + File.separator + "data" + File.separator + "train" + File.separator + "template" + File.separator + "template1";
		String testFile = dir.getCanonicalPath() + File.separator + "data" + File.separator + "train" + File.separator + "input" + File.separator + "A 00 (1).txt";
		String modelFile = dir.getCanonicalPath() + File.separator + "data" + File.separator + "train" + File.separator + "model" + File.separator + "model";
		System.out.println(testFile);
		train(testFile,templateFile,modelFile);
	}
	
	public static void train(String testFile,String template,String modelName) throws IOException{
		System.out.println("train");
		File dir = new File(".");
		Process process = new ProcessBuilder(dir.getAbsolutePath() + File.separator + "crf_learn.exe",template,testFile,modelName).start();
		InputStream is = process.getInputStream();
		InputStreamReader isr = new InputStreamReader(is);
		BufferedReader br = new BufferedReader(isr);
		String line;

		System.out.printf("Output of running is:");

		while ((line = br.readLine()) != null) {
		  System.out.println(line);
		}
		System.out.println("finished");
	}
}
