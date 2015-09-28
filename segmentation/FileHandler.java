import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.util.HashSet;
import java.util.Random;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FileHandler {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		File dir = new File(".");
		String file = dir.getAbsolutePath() + File.separator +"data" + File.separator + "preprocess" + File.separator + "test.html";
		String out = dir.getAbsolutePath() + File.separator +"data" + File.separator + "preprocess" + File.separator;
		genFileFromSQL(file,out);
	}

	public static void genFileFromSQL(String file,String out) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(new File(file)), "UTF-8"));
		boolean rand = true;
		int max = 261;
		Set<Integer> set = new HashSet<Integer>();
		Random randomGenerator = new Random();
		randomGenerator.setSeed(1);
		String line = null;
		int index = 0;
		File dir1 = new File(out + File.separator + "human");
		if(!dir1.exists()){
			dir1.mkdirs();
		}
		File dir2 = new File(out + File.separator + "raw");
		if(!dir2.exists()){
			dir2.mkdirs();
		}
		while((line = br.readLine())!= null){
			Pattern p = Pattern.compile("<td class='normal' valign='top'>(.+)</td>");
			Matcher matcher1 = p.matcher(line);
			while (matcher1.find()) {
				index++;
				if(rand){
					index = randomGenerator.nextInt(max);
					while(set.contains(index)){
						index = randomGenerator.nextInt(max);
					}
					set.add(index);
				}
				System.out.println(index + line);
				BufferedWriter bw1 = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(dir1.getAbsolutePath() + File.separator + index + ".txt"),"UTF-8"));
				BufferedWriter bw2 = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(dir2.getAbsolutePath() + File.separator + index + ".txt"),"UTF-8"));
				String newline = line.replaceAll("<td class='normal' valign='top'>(.+)</td>", "$1");
				bw1.write(newline);
				bw2.write(newline.replaceAll("\\s", ""));
				bw1.close();
				bw2.close();
			}
		}
		br.close();
	}


}
