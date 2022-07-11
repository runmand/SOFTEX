import java.io.FileInputStream;
import java.io.FileOutputStream;

public class test {
    public static void main(_String[] args) {

        ArrayList < Object > list = new ArrayList();

        ObjectOutputStream objOutput = new ObjectOutputStream();
        FileOutputStream objFile = new FileOutputStream(objOutput);
        objFile.writeObject(lista);
        objFile.close();



        ObjectInputStream objInput = new ObjectInputStream();
        FileInputStream objInputFile = new FileInputStream(objInput);
        lista = (ArrayList < Object > ) objInput.readObject();
        objInputFile.close();
    }
}