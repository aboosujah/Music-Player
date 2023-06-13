//import java.util.Scanner;

class Add{
	Add(int x, int y){
		System.out.println(x+"+"+y+"=" + (x+y));
	}
	
	Add(int x, int y, int z){
		System.out.println(x +"+"+ y + "+"z +"=" +(x+y+z));
	}
}
public class Addition{	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		System.out.println("How many numers to add = ");
		int n = scan.nextInt();
		
		if(n==2){
			System.out.println("Enter number 1 =");
			int p = scan.nextInt();
			System.out.println("Enter number 1 =");
			int q = scan.nextInt();
			Add obj1 = new Add(p,q);
		}
		
		if(n==3){
			System.out.println("Enter number 1 =");
			int p = scan.nextInt();
			System.out.println("Enter number 1 =");
			int q = scan.nextInt();
			System.out.println("Enter number 3 =");
			int r = scan.nextInt();
			Add obj2 = new Add(p,q,r);
		}
	}
}
	
