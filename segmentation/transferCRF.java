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
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class transferCRF {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		System.out.println("a" + "\u0009" + notationWordSeg.SINGLE.getSign());
		System.out.println("a" + "\u0009" + notationWordSeg.BEGIN.getSign());
		System.out.println("a" + "\u0009" + notationWordSeg.INSIDE.getSign());
		File dir = new File(".");
		String input = dir.getCanonicalPath() + File.separator + "data" + File.separator + "test" + File.separator +"human";
		String output = dir.getCanonicalPath() + File.separator + "data" + File.separator + "test" + File.separator + "out";
		String output2 = dir.getCanonicalPath() + File.separator + "data" + File.separator + "test" + File.separator + "out2";
		String dict =  dir.getCanonicalPath() + File.separator + "data" + File.separator + "dict" + File.separator + "test.txt";
		String targetName = "A 00 (1).txt";
		normal2crfWithDict(input,output,targetName,dict,true);
		crf2normal(output,output2,targetName,2);

	}

	public static void normal2crfGroupTest(String input, String output,String[] targetNames) throws FileNotFoundException, Exception{
		normal2crfGroup(input,output,targetNames,"",false,false);
	}

	public static void normal2crfGroupTestWithDict(String input, String output,String[] targetNames, String dict) throws FileNotFoundException, Exception{
		normal2crfGroup(input,output,targetNames,dict,false,true);
	}

	public static void normal2crfGroupTrain(String input, String output, String[] targetNames) throws FileNotFoundException, Exception{
		normal2crfGroup(input,output,targetNames,"",true,false);
	}

	public static void normal2crfGroupTrainWithDict(String input, String output, String[] targetNames, String dict) throws FileNotFoundException, Exception{
		normal2crfGroup(input,output,targetNames,dict,true,true);
	}

	public static void normal2crfGroup(String input, String output, String[] targetNames, String dict, boolean train, boolean useDict) throws FileNotFoundException, Exception{
		File dir2 = new File(output);
		if(!dir2.exists()){
			dir2.mkdirs();
		}
		for(String targetName: targetNames){
			File dir = new File(input + File.separator + targetName);
			if(!dir.exists()){
				System.err.println(dir.getAbsolutePath() + " is not found!");
				continue;
			}
			if(train && useDict){
				normal2crfWithDict(input,output,targetName,dict,true);
			}else if(train){
				normal2crf(input,output,targetName,true);
			}else if(useDict){
				normal2crfWithDict(input,output,targetName,dict,false);
			}else{
				normal2crf(input,output,targetName,false);
			}
		}
	}

	public static void crf2normalGroup(String input, String output,String[] targetNames, int featNum) throws FileNotFoundException, Exception{
		File dir2 = new File(output);
		if(!dir2.exists()){
			dir2.mkdirs();
		}
		for(String targetName: targetNames){
			File dir = new File(input + File.separator + targetName);
			if(!dir.exists()){
				System.err.println(dir.getAbsolutePath() + " is not found!");
				continue;
			}
			crf2normal(input,output,targetName,featNum);

		}

	}

	public static void normal2crf(String input,String output,String targetName, boolean forTrain) throws Exception, FileNotFoundException{
		File dir = new File(input + File.separator + targetName);
		if(!dir.exists()){
			System.err.println(dir.getAbsolutePath() + " is not found!");
			return;
		}
		File dir2 = new File(output);
		if(!dir2.exists()){
			dir2.mkdirs();
		}
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(new File(input + File.separator + targetName)), "UTF-8"));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(output + File.separator + targetName)),"UTF-8"));
		String line;		
		if(forTrain){
			int lastLen = 0;
			while((line = br.readLine()) != null){
				System.out.println(line + " len is " + line.length());
				for(int i = 0; i < line.length(); i++){
					if(Character.isWhitespace(line.charAt(i))){
						lastLen = 0;
					}else{
						lastLen++;
						bw.write(line.charAt(i));
						//for tab 
						bw.write("\u0009");
						if(i == line.length() -1){
							if(lastLen == 1){
								bw.write(notationWordSeg.SINGLE.getSign());
							}else{
								bw.write(notationWordSeg.INSIDE.getSign());
							}
						}else if(Character.isWhitespace(line.charAt(i + 1))){
							if(lastLen == 1){
								bw.write(notationWordSeg.SINGLE.getSign());
							}else{
								bw.write(notationWordSeg.INSIDE.getSign());
							}
						}else{
							if(lastLen == 1){
								bw.write(notationWordSeg.BEGIN.getSign());
							}else{
								bw.write(notationWordSeg.INSIDE.getSign());
							}
						}
						bw.newLine();
					}
					if(isSentenceSign(line.charAt(i))){
						bw.newLine();
					}
				}
				bw.newLine();
			}
		}else{
			while((line = br.readLine()) != null){
				for(int i = 0; i < line.length(); i++){
					//if it is not a white space write the single char into file and get new line
					//if it is a sentence end sign, write a extra new line
					if(!Character.isWhitespace(line.charAt(i))){
						bw.write(line.charAt(i));
						bw.newLine();
					}
					if(isSentenceSign(line.charAt(i))){
						bw.newLine();
					}
				}
				bw.newLine();
			}
		}
		br.close();
		bw.close();

	}

	public static void normal2crfWithDict(String input,String output,String targetName, String dictPath, boolean forTrain) throws Exception, FileNotFoundException{		
		File dir = new File(input + File.separator + targetName);
		if(!dir.exists()){
			System.err.println(dir.getAbsolutePath() + " is not found!");
			return;
		}
		File dir2 = new File(output);
		if(!dir2.exists()){
			dir2.mkdirs();
		}
		HashSet<String> dict = (HashSet<String>) IOmanager.loadDict(dictPath);

		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(new File(input + File.separator + targetName)), "UTF-8"));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(output + File.separator + targetName)),"UTF-8"));
		String line;
		if(forTrain){
			int lastLen = 0;
			String word = null;
			while((line = br.readLine()) != null){
				System.out.println(line + " len is " + line.length());
				for(int i = 0; i < line.length(); i++){
					if(Character.isWhitespace(line.charAt(i))){
						lastLen = 0;
					}else{
						lastLen++;
						bw.write(line.charAt(i));
						//for tab
						if(lastLen == 1){
							word = "";
							//get the word and next starting point 
							for(int j = i; j < line.length(); j++){
								if(Character.isWhitespace(line.charAt(j))){
									word = line.substring(i,j);
									break;
								}else if(j == line.length() - 1){
									word = line.substring(i,j + 1);
								}
							}
							if(dict.contains(word)){
								bw.write("\u0009" + notationDict.BEGIN.getSign());
							}else{
								bw.write("\u0009" + notationDict.OutOfV.getSign());
							}
						}else{
							if(dict.contains(word)){
								bw.write("\u0009" + notationDict.INSIDE.getSign());
							}else{
								bw.write("\u0009" + notationDict.OutOfV.getSign());
							}
						}

						if(i == line.length() -1){
							if(lastLen == 1){
								bw.write("\u0009" + notationWordSeg.SINGLE.getSign());
							}else{
								bw.write("\u0009" + notationWordSeg.INSIDE.getSign());
							}
						}else if(Character.isWhitespace(line.charAt(i + 1))){
							if(lastLen == 1){
								bw.write("\u0009" + notationWordSeg.SINGLE.getSign());
							}else{
								bw.write("\u0009" + notationWordSeg.INSIDE.getSign());
							}
						}else{
							if(lastLen == 1){
								bw.write("\u0009" + notationWordSeg.BEGIN.getSign());
							}else{
								bw.write("\u0009" + notationWordSeg.INSIDE.getSign());
							}
						}
						bw.newLine();
					}
					if(isSentenceSign(line.charAt(i))){
						bw.newLine();
					}
				}
				bw.newLine();
			}
		}else{
			int max = 0;
			int wordStartIndex =0 ;
			for(String word : dict){
				if(word.length() > max){
					max = word.length();
				}
			}
			while((line = br.readLine()) != null){
				wordStartIndex = 0;
				for(int i = 0; i < line.length(); i++){
					//if it is not a white space write the single char into file and get new line
					//if it is a sentence end sign, write a extra new line
					if(!Character.isWhitespace(line.charAt(i))){
						bw.write(line.charAt(i));
						if(wordStartIndex == i){ //already in
							for(int j = Math.min(i + max ,line.length()); j>= i; j--){
								wordStartIndex = j;
								if(dict.contains(line.substring(i,j))){
									break;
								}
							}
							if(wordStartIndex > i)
								bw.write("\u0009"+ notationDict.BEGIN.getSign());
							else{
								bw.write("\u0009"+ notationDict.OutOfV.getSign());
								wordStartIndex++;
							}
						}else{
							bw.write("\u0009"+ notationDict.INSIDE.getSign());
						}
						bw.newLine();
					}else{
						wordStartIndex = i + 1;
					}
					if(isSentenceSign(line.charAt(i))){
						bw.newLine();
						wordStartIndex =  i + 1;
					}
				}
				bw.newLine();
			}
		}
		br.close();
		bw.close();

	}


	public static void crf2normal(String input,String output,String targetName, int featNum) throws Exception, FileNotFoundException{
		File dir = new File(input + File.separator + targetName);
		if(!dir.exists()){
			System.err.println(dir.getAbsolutePath() + " is not found!");
			return;
		}
		File dir2 = new File(output);
		if(!dir2.exists()){
			dir2.mkdirs();
		}
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(new File(input + File.separator + targetName)), "UTF-8"));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(output + File.separator + targetName)),"UTF-8"));
		String line;		
		while((line = br.readLine())!= null){
			if(line.length() == 0){
				bw.newLine();
			}else{
				String[] split = line.split("\u0009");
				if(split != null && split.length == featNum + 1){
					if(split[featNum].equals(notationWordSeg.SINGLE.getSign()) || split[featNum].equals(notationWordSeg.BEGIN.getSign())){
						bw.write("\u0020");
					}
					bw.write(split[0]);
				}
				//				if(line.length() == 3 && (line.charAt(2) == notationWordSeg.SINGLE.getSign() || line.charAt(2) == notationWordSeg.BEGIN.getSign())){ 
				//					bw.write("\u0020");
				//				}
				//				bw.write(line.charAt(0));		
			}
		}
		br.close();
		bw.close();

	}




	private static boolean isSentenceSign(char sign){
		Set<Character> signs = new HashSet<Character>(Arrays.asList('\u3002','\uFF1F','\uFF01', '\uFF1B','\u2026'));
		return signs.contains(sign);
	}
}


