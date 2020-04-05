import java.io.*;

public class Change {
    public static void main(String[] args) {
        // check args
        int version = 0;
        if(args.length == 1){
            version = Integer.parseInt(args[0]);
        }
        else{
            System.out.println("Please input yur version number.");
            return;
        }
        try {
            FileReader inputFile = new FileReader("version-0" + version + ".acceptedRate");
            BufferedReader br = new BufferedReader(inputFile);
            FileWriter outputFile = new FileWriter("version-0" + version + "-acc.csv");
            BufferedWriter bw = new BufferedWriter(outputFile);
            String s = br.readLine();
            // head
            bw.write("epoch,loss,train-acc,test-acc");
            bw.newLine();
            while (s != null) {
                if(s.charAt(0) != '#'){
                    String a[] = s.split(",");
                    String output = "";
                    String t;
                    // eposh
                    t = a[0].substring(1, a[0].indexOf("]"));
                    output += t + ",";
                    // loss
                    t = a[1].substring(a[1].indexOf(":") + 2);
                    output += t + ",";
                    // train-acc
                    t = a[2].substring(a[2].indexOf(":") + 2);
                    output += t + ",";
                    //test-acc
                    t = a[3].substring(a[3].indexOf(":") + 2);
                    output += t;
                    bw.write(output);
                    bw.newLine();
                }
                s = br.readLine();
            }
            br.close();
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
