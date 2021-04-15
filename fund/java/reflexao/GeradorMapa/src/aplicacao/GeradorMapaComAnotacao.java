package aplicacao;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Map;

public class GeradorMapaComAnotacao {

	@Retention(RetentionPolicy.RUNTIME)
	public @interface Ignorar {
	}
	
	@Retention(RetentionPolicy.RUNTIME)
	public @interface NomePropriedade {
		String value();
	}
	
	public static Map<String, Object> gerarMapaComAnotacao(Object o) {
		Class<?> classe = o.getClass();
		Map<String, Object> mapa = new HashMap<>();
		for (Method m: classe.getMethods()) {
			try {
				if (isGetter(m)) {
					String propriedade = null;
					if (m.isAnnotationPresent(NomePropriedade.class)) {
						propriedade = m.getAnnotation(NomePropriedade.class).value(); 
					} else {
						propriedade = deGetterParaPropriedade(m.getName());
					}
					
					Object valor = m.invoke(o);
					mapa.put(propriedade,  valor);
				}
			} catch (Exception e) {
				throw new RuntimeException("Problema ao gerar o mapa", e);
			}
		}
		return mapa;
	}
	
	private static boolean isGetter(Method m) {
		return m.getName().startsWith("get") &&
				m.getReturnType() != void.class &&
				m.getParameterTypes().length == 0 &&
				!m.isAnnotationPresent(Ignorar.class);
	}
	
	private static String deGetterParaPropriedade(String nomeGetter) {
		StringBuffer retorno = new StringBuffer();
		retorno.append(nomeGetter.substring(3, 4).toLowerCase());
		retorno.append(nomeGetter.substring(4));
		return retorno.toString();
	}
	
}