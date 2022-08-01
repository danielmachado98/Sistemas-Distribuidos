import java.io.IOException;
import java.io.UnsupportedEncodingException;
import javax.swing.JOptionPane;

public class Cliente02 {
    public static void main(String[] args) throws IOException, UnsupportedEncodingException {

        String nome;
		nome = JOptionPane.showInputDialog(null,"Digite o Nome:","Nome",JOptionPane.INFORMATION_MESSAGE);
		
		String sexo;
		sexo = JOptionPane.showInputDialog("Digite o Sexo:");
		
		int idade;
		idade = Integer.parseInt(JOptionPane.showInputDialog("Digite a Idade:"));
	
		Object[] possibleValues = { "First", "Seçond", "Thírd" };
		Object selectedValue = JOptionPane.showInputDialog(null, "Choose one", "ola!",JOptionPane.INFORMATION_MESSAGE, null, possibleValues, possibleValues[0]);
	
		Object[] options = { "Masculino", "Feminino" };
		Object selectedoption = JOptionPane.showOptionDialog(null, "Selecione o Sexo","Sexo",JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, options[0]);

		
	
		String message = "nome: " +nome+ " sexo: " +sexo+ " idade: " +idade+ " selecionado: " +selectedValue+ " option: " +selectedoption;
		JOptionPane.showMessageDialog(null,message);
    }
}