import java.util.Random;
import java.util.Scanner;
public class SumRandom{
	public static void main(String[] args){
		Scanner input=new Scanner(System.in);
		Random rand=new Random();
		System.out.print("enter the sum of the random generated number:");
		int userinput=input.nextInt();
		int number=rand.nextInt(100);
		int number2=rand.nextInt(100);
		int add=number+number2;
		if(userinput==add){
			System.out.print("true");
		}
		else{
			System.out.print("false");
		}
	}
}