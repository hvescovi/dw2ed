package exemplo4.modelo;

public class Author {

	public Integer AuthorID;
	public String FirstName;
	public String LastName;
	
	@Override
	public String toString() {
		return String.format("(%d) %s %s",
				AuthorID, FirstName, LastName);
	}
}
