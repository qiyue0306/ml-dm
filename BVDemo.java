public class BVDemo{

	private static double[] x = new double[2];
	private static double[] y = new double[2];
	
	private static void generateData() {
		x[0] = Math.random()*2-1; x[1] = Math.random()*2-1;
		y[0] = Math.sin(x[0]*Math.PI); y[1] = Math.sin(x[1]*Math.PI);
	}
	
	private static void firstModel(){
//		H0: h(x)=b0
		double b0 = (y[0]+y[1])/2;
		double biasSq0 = Math.pow((y[0]-b0),2) + Math.pow((y[1]-b0), 2);
		double var0 = 0;
		System.out.printf("H0, bias squared: %.3f, variance: %.3f; ",biasSq0, var0);
	}
		
	private static void secondModel(){
//		H1: h(x)=a1*x + b1	
		double a1 = (y[0]-y[1])/(x[0]-x[1]);
		double b1 = y[0] - a1*x[0];
		double biasSq1 = Math.pow((y[0]-a1*x[0]-b1),2) + Math.pow((y[1]-a1*x[1]-b1),2);
		double var1 =  Math.pow((a1*x[0]+b1)-(y[0]+y[1]/2),2) + Math.pow((a1*x[1]+b1)-(y[0]+y[1]/2),2);
		System.out.printf("H1, bias squared: %.3f, variance: %.3f\n",biasSq1, var1);
	}
	
	/*
	private static void testFirstModel(){
		generateData();
		double biasSq0 = Math.pow((y[0]-b0),2) + Math.pow((y[1]-b0), 2);
		double var0 = 0;
		double biasSq1 = Math.pow((y[0]-a1*x[0]-b1),2) + Math.pow((y[1]-a1*x[1]-b1),2);
		double var1 =  Math.pow((a1*x[0]+b1)-(y[0]+y[1]/2),2) + Math.pow((a1*x[1]+b1)-(y[0]+y[1]/2),2);
		System.out.printf("H0, bias squared: %.3f, variance: %.3f; ",biasSq0, var0);
	}
	
	*/
	public static void main(String[] args) {
		for (int i=1; i<=10; i++) {
			System.out.println("DataSet "+i);
			generateData();
			firstModel();
			secondModel();
		}
	}
}

