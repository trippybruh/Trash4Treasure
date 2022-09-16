
import java.util.*; 

public class User {

	private final String name_surname;
	private final String user_name;
	protected final String psw;
	protected final String email;
	private int age;
	private boolean trusted;
	@SuppressWarnings("unused")
	private double score;
	private Date account_creation;
	private Date last_access;
	
	/* Mobilio da dare via e dato via */
	private LinkedList<ForniturePiece> isAvailable;  /*realmente dispoibili*/
	private LinkedList<ForniturePiece> isTaken;			
	
	/* Mobilio d'interesse e già ottenuto */
	private LinkedList<ForniturePiece> isWished;    /*realmente dispoibili*/
	private LinkedList<ForniturePiece> hasTaken;
	 
	
	
	public User (String name_surname, String user_name, String psw, String email, int age) {
		
		this.name_surname = name_surname;
		this.user_name = user_name;
		this.psw = psw;
		this.email = email;
		this.age = age;
		this.trusted = false;
		this.account_creation = new Date();
		
		this.isAvailable = new LinkedList<ForniturePiece>();
		this.isTaken = new LinkedList<ForniturePiece>();
		this.isWished = new LinkedList<ForniturePiece>();
		this.hasTaken = new LinkedList<ForniturePiece>();
	}
	
	public void updateSold (ForniturePiece A) throws objectNotAvaliableExc {
		
		if (isAvailable.remove(A)) {
			isTaken.add(A);
		} else throw new objectNotAvaliableExc();
	}
	
	public void updateBuy (ForniturePiece A) {
		isWished.remove(A);
		hasTaken.add(A);
	}
	
	public void newWish(ForniturePiece A) {
		isWished.add(A);
	}
	
	public void newAvailable(ForniturePiece A) {
		isAvailable.add(A);
	}
	
	public void remWish(ForniturePiece A) {
		isWished.remove(A);
	}
	
	public void remAvailable(ForniturePiece A) {
		isAvailable.remove(A);
	}
	
	public void formatWish() {
		isWished.clear();
	}
	
	public String userDetails() {
		return "COMPLETE NAME: " + name_surname + "\n" + "USERNAME: " + user_name + "\n" + "EMAIL USED: " + email + "\n" + "AGE: " + age + "\n" + "TRUSTED USER: " + trusted + "\n" + "FIRST LOGIN: " + account_creation.toString() + "\n" + "LAST LOGIN: " + last_access.toString() + "\n";
	}
	
	public String userActivity() {
		return isAvailable.toString() + "\n" + isTaken.toString() + "\n" + isWished.toString() + "\n" + hasTaken.toString();
	}
	
	
}
