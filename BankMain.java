public class BankMain {
    public static void main(String[] args){

        Account cust1 = new Account();
        cust1.deposit(500);

        Account cust2 = new Account();
        cust2.withdraw(400);

        System.out.print("Cust1 has a balance of ");
        System.out.println(cust1.getBalance());

        System.out.print("Cust2 has a balance of ");
        System.out.println(cust2.getBalance());

    }
}
