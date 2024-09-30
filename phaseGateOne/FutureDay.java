import java.util.Scanner;
public class FutureDay{
	public static void main(String[] args){
		Scanner input=new Scanner(System.in);
		System.out.print("enter today's day:");
		int day=input.nextInt();
		System.out.print("enter the numbers of days elapsed since today:");
		int elapsed_day=input.nextInt();

		int future_day=day+elapsed_day

		if (future_day==0 || future_day==7){
			System.out.printf("the future day is%d",Sunday);
		}

if (future_day==1 || future_day==8){
	System.out.printf("the future day is%d",Monday);
}

if (future_day==2 || future_day==9){
	System.out.printf("the future day is%d",Tuesday);
}

if( future_day==3 || future_day==10 ){
	System.out.printf("the future day is%d",Wednesday);
}

if (future_day==4 || future_day==11){
	System.out.printf("the future day is%d",Thursday);
}

if (future_day==5 || future_day==12){
	System.out.printf("the future day is%d",Friday);
}

		if (future_day==6 || future_day==13){
			System.out.printf("the future day is%d",Saturday);
}
		}
}