import java.awt.List;
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
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class crossValidation {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		cross();
		System.out.println("finished!");
	}

//	public static void normalTrain() throws Exception, Exception{
//		int rand = 4;
//		File dir = new File(".");
//		String[] dictNames = {"generalchinesewords"};
//		String[] targetNames = getRandNames(rand);
//
//		String ranListPath = dir.getCanonicalPath() + File.separator + "data" + File.separator + "splits" + File.separator + "rand" + rand;
//		File folder = new File(ranListPath);
//		File[] fileList = folder.listFiles();
//		if(fileList != null){
//			for(File child : fileList){
//				File s = new File(child.getAbsolutePath());
//				File d = new File(dir.getCanonicalFile() + File.separator+ "data" + File.separator + "input" + File.separator+ child.getName());
//				System.out.println("copy from "+ s.getAbsolutePath() + "to " + d.getAbsolutePath());
//				Files.copy(s.toPath(), d.toPath(),StandardCopyOption.REPLACE_EXISTING);
//			}
//		}
//
//		System.out.println("load Files" + targetNames.length);
//		//String[] targetNames = {"A 00 (16).txt"};
//		String modelName = dir.getCanonicalPath() + File.separator + "data" + File.separator + "train" + File.separator +"cross"+ File.separator + "final";
//		String outputPath = dir.getCanonicalPath() + File.separator + "data" + File.separator + "result" + File.separator +"stfdnlp" + File.separator +"cross" + File.separator + "final";
//
//		for(String dictName: dictNames){
//			File out = new File(outputPath + File.separator + dictName);
//			for(File temp : out.listFiles()){
//				temp.delete();
//			}
//
//			crossValidation.trainData(targetNames, dictName, modelName, outputPath);
//		}
//	}

	public static void cross() throws Exception{
		File dir = new File(".");
		File temp;
		File fout = new File(dir.getCanonicalPath() + File.separator + "data" + File.separator +"cross" + File.separator + "crossValidationSummaryCrf++WithDictsRand261.txt");
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(fout),"UTF-8"));;
		String[] dictNames = {"none", "medical","generalchinesewords","all"};
		//String[] dictNames = {"generalchinesewords"};
		
		int trainTimes = 5;
		int totalNum = 261;
		
		
		String[] targetNames = IOmanager.getTargetNames(1,totalNum);
		//convert all training set into crf input format
		String humanPath = dir.getCanonicalPath() + File.separator + "data" + File.separator + "cross" + File.separator + "human";
		String rawPath =  dir.getCanonicalPath() + File.separator + "data" + File.separator + "cross" + File.separator+ "raw";
		for(String dictName : dictNames){
			String humanCRF = dir.getCanonicalPath() + File.separator + "data" + File.separator + "cross" + File.separator+ "humanCRF"+ File.separator + dictName;
			String dictPath = dir.getCanonicalPath() + File.separator+ "data" + File.separator + "dict" + File.separator + dictName + ".txt";
			transferCRF.normal2crfGroupTrainWithDict(humanPath,humanCRF,targetNames,dictPath);
			CWSReport rep = new CWSReport();
			float overAllF = 0;
			
			for(int i = 1; i <= trainTimes; i++){
				//targetName
				System.out.println("\n");
				System.out.println("start is " + ((i-1)*10 + 1) + "end is "+ ((i-1)*10 + 10));
				String[] allSet = IOmanager.getTargetNames(1,totalNum);
				String[] testSet = IOmanager.getTargetNames((i-1)* (totalNum / trainTimes)  + 1, (i-1)* (totalNum / trainTimes) + (totalNum / trainTimes));
				
				final ArrayList<String> list =  new ArrayList<String>();
				final ArrayList<String> list2 =  new ArrayList<String>();
				Collections.addAll(list, allSet);
				Collections.addAll(list2, testSet);
				list.removeAll(list2);
				String[] trainSet = list.toArray(new String[list.size()]);
				for(String item : testSet){
					System.out.println("testSet" + item);
				}
				for(String item : trainSet){
					System.out.println("trainSet" + item);
				}
				
				
				
				//String modelName = dir.getCanonicalPath() + File.separator + "data" + File.separator + "train" + File.separator +"cross" + File.separator + Integer.toString(i);
				System.out.println("train\t" + "set" + Integer.toString(i) + "\t");
				//if(true) continue;
				
				//merge all train set into one train file.
				String trainPath = dir.getCanonicalPath() + File.separator + "data" + File.separator + "cross" + File.separator + dictName + File.separator + i;
				temp = new File(trainPath);
				if(!temp.exists()){
					temp.mkdirs();
				}
				trainPath = trainPath + File.separator + i + ".txt";
				IOmanager.mergeFile(humanCRF, trainPath, trainSet);
				
				
				//set model path & template file
				String modelName = dir.getCanonicalPath() + File.separator + "data" + File.separator + "cross" + File.separator + dictName + File.separator + i + File.separator + "model" + i + ".md";
				String templateFile = dir.getCanonicalPath() + File.separator + "data" + File.separator + "train" + File.separator + "template" + File.separator + "template1";
				//train the model
				trainCRF.train(trainPath,templateFile,modelName);
				
				//transfer test normal file to crf format
				String testPathNormal = dir.getCanonicalPath() + File.separator + "data" + File.separator + "cross" + File.separator + dictName + File.separator + i + File.separator + "Normal";
				temp = new File(testPathNormal);
				if(!temp.exists()){
					temp.mkdirs();
				}
				for(String test: testSet){
					File tp = new File(rawPath + File.separator + test);
					if(tp.exists()){
						Files.copy(tp.toPath(), new File (testPathNormal + File.separator + test).toPath(), StandardCopyOption.REPLACE_EXISTING);
					}
				}
				
				String testPathCRF = dir.getCanonicalPath() + File.separator + "data" + File.separator + "cross" + File.separator + dictName + File.separator + i + File.separator + "CRF";
				transferCRF.normal2crfGroupTestWithDict(testPathNormal, testPathCRF,testSet,dictPath);
				
				//process the file
				String testPathRes = dir.getCanonicalPath() + File.separator + "data" + File.separator + "cross" + File.separator + dictName + File.separator + i + File.separator  + "result";
				useCRF.processAll(modelName, testSet, testPathCRF, testPathRes);
				
				//transfer crf to normal files
				String testPathResNormal = dir.getCanonicalPath() + File.separator + "data" + File.separator + "cross" + File.separator + dictName + File.separator + i + File.separator  + "resultNormal";
				transferCRF.crf2normalGroup(testPathRes, testPathResNormal, testSet, 2);
				
				String toolName = "crf++";
				String debug = dir.getCanonicalPath() + File.separator + "data" + File.separator +"cross";
				
				bw.write("***************************************************************************************************\n");
				bw.write("\t Tools Name :" + toolName + "\t Dict Name : " + dictName + "\n");
				bw.write("\t Model Path :" + modelName  + "\n");
				bw.write("***************************************************************************************************\n");
				bw.write(rep.process(testSet,toolName,dictPath,testPathResNormal,humanPath,debug));	
				//public String process(String[] targetNames, String toolName, String dictPath, String toolResultPath, String humanResultPath) throws IOException{
				overAllF += rep.getOverAllF();
			}
			bw.write("for Dict : " + dictName + " the overAll F after cross validation is " + (overAllF /trainTimes ));
			bw.write("***************************************************************************************************\n");
			bw.write("***************************************************************************************************\n");
			bw.write("***************************************************************************************************\n");
			bw.write("***************************************************************************************************\n");
			bw.newLine();
			bw.newLine();
			bw.newLine();

		}

		bw.close();
	}

	

}
