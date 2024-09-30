import java.util.Scanner;
public class Arrange{
	public static void main(String[] args){
		Scanner input=new Scanner(System.in);
		System.out.print("enter first number:");
		int firstNumber=input.nextInt();
		System.out.print("enter second number:");
		int secondNumber=input.nextInt();
		System.out.print("enter third number:");
		int thirdNumber=input.nextInt();

	if (firstNumber>secondNumber && secondNumber>thirdNumber){
	System.out.println(thirdNumber+secondNumber+firstNumber);
	}

	if (secondNumber>firstNumber && firstNumber>thirdNumber){
	System.out.println(thirdNumber+firstNumber+secondNumber);
	}

	if (thirdNumber>firstNumber && firstNumber>secondNumber){
	System.out.println(secondNumber+firstNumber+thirdNumber);
	}

	if (secondNumber>thirdNumber && thirdNumber>firstNumber){
	System.out.println(firstNumber+thirdNumber+secondNumber);
	}

	if (thirdNumber>secondNumber && secondNumber>firstNumber){
	System.out.println(firstNumber+secondNumber+thirdNumber);
	}

	if (firstNumber>thirdNumber && thirdNumber>secondNumber){
	System.out.println(secondNumber+thirdNumber+secondNumber);
	}

	}
}