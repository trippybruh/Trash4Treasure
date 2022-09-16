import java.util.*;

public class ForniturePiece {
	
	private String title;
	private String description;
	private String owner;
	private String next_owner;
	private Date published;
	private double lenght;
	private double height;
	private double width;
	private double volume;
	private boolean sold;
	
	
	public ForniturePiece(String title, String description, String owner, double lenght, double height, double width) {
		
		this.title = title;
		this.description = description;
		this.owner = owner;
		this.next_owner = "None";
		this.published = new Date();
		this.lenght = lenght;
		this.height = height;
		this.width = width;
		this.volume = lenght*height*width;
		this.sold = false;
		
	}
	
	public void updateStatus (String new_owner) {
		sold = true;
		next_owner = new_owner;
	}
	
	public String toString() {
		String str = "TITLE: " + title + "\n" + "DESCRIPTION: " + description + "\n" + "PUBLISHING DATE: " + published.toString() + "\n" + "ORGINAL OWNER: " + owner + "\n" + "DIMENSIONS: " + lenght + "x" + height + "x" + width + " = " + volume + "\n";
		if (sold) {
			str += "STAUS: SOLD" + "\n" + "NEW OWNER: " + next_owner;
 		} else str += "STAUS: UNSOLD";
		return str;
	}
}
