package reflexao;

import java.lang.annotation.Annotation;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.reflect.AnnotatedElement;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class ExemplosAnotacoes {

	//anotação com valor (parâmetro)
	// definida no escopo da classe apenas
	@Retention(RetentionPolicy.RUNTIME)
	@Target({ElementType.FIELD})
	public @interface Metadado4 {
		int valor();
	}
	
	@Metadado
	String atributoA;
	
	@Metadado2
	String atributoB;
	
	@Metadado3
	public String metodoA() {
		return "ok";
	}	
	
		
	@Metadado4(valor = 10)
	String atributoC;
	
	public static void main(String args[]) {
		System.out.println("Exemplos de anotações");
		Class<?> c = ExemplosAnotacoes.class;
		
		try {
			Field f = c.getDeclaredField("atributoC");
			if (f.isAnnotationPresent(Metadado4.class)) {
				Metadado4 m4 = f.getAnnotation(Metadado4.class);
				System.out.println("Valor no metadado4: " + m4.valor());
			}
		} catch (NoSuchFieldException | SecurityException e) {
			e.printStackTrace();
		}
		
		// percorrer atributos
		for (Field f : c.getDeclaredFields()) {
			System.out.println("Anotações do: "+f.getName());
			// obter anotações do atributo
			Annotation[] ans = f.getAnnotations();
			for (Annotation an : ans) {
				// exibir nome da anotação
				System.out.println(an.annotationType().getName());
			}
		}
			
	}
}
