import java.util.*;

//Mark Schelkoph
//Assignment 4

class Main {
  public static void main(String[] args) 
  {
    ArrayList<Account> accounts = new ArrayList<Account>();

    CheckingAccount a1 = new CheckingAccount(100, 1000);
    SavingsAccount a2 = new SavingsAccount(200, 2.5);
    SavingsAccount a3 = new SavingsAccount(1600, 5.0);
    CheckingAccount a4 = new CheckingAccount(454, 325);

    accounts.add(a1);
    accounts.add(a2);
    accounts.add(a3);
    accounts.add(a4);

    System.out.println("\nstarting account info:\n");
    for (Account a : accounts)
    {
      System.out.println(a + "\n");
    }

    accounts.get(0).deposit(150);
    accounts.get(1).withdraw(100);

    System.out.println("\naccount info after depost/withdraw:\n");
    for (Account a : accounts)
    {
      System.out.println(a + "\n");
    }

    ((CheckingAccount)accounts.get(0)).orderChecks();
    ((SavingsAccount)accounts.get(1)).Compound();
    ((SavingsAccount)accounts.get(2)).Compound();
    ((CheckingAccount)accounts.get(3)).orderChecks();

    Collections.sort(accounts);
    
    System.out.println("\naccounts after sort and method calls:");
    for (Account a : accounts)
    {
      System.out.println(a + "\n");
    }
  }
}