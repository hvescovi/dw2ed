package exemplo;

// hibernate zip downloaded from
// https://hibernate.org/orm/releases/5.4/ (zip file)

public class Product {

	private String stockNumber;
	private String manufacturer;
	private String item;
	private double unitPrice;

	public Product(String stock, String man, String it, double unit) {
		stockNumber = stock;
		manufacturer = man;
		item = it;
		unitPrice = unit;
	}
	
	public Product() {}
		
	public String getStockNumber() {
		return stockNumber;
	}

	public void setStockNumber(String stockNumber) {
		this.stockNumber = stockNumber;
	}

	public String getManufacturer() {
		return manufacturer;
	}

	public void setManufacturer(String manufacturer) {
		this.manufacturer = manufacturer;
	}

	public String getItem() {
		return item;
	}

	public void setItem(String item) {
		this.item = item;
	}

	public double getUnitPrice() {
		return unitPrice;
	}

	public void setUnitPrice(double unitPrice) {
		this.unitPrice = unitPrice;
	}
	
	
	
}
