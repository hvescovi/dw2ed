package reflexao;

public class RecuperandoPeloObjeto {

	public static void main(String args[]) {
		Number object = new Integer(100);
		Class <? extends Number> c = object.getClass();
		System.out.println(c.getName());
		System.out.println(object);
		
		Integer i = new Integer(100);
		Class <?> ni = object.getClass();
		System.out.println(ni.getName());
		System.out.println(i);
		
		
	}
	
}
