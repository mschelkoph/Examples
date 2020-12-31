import javax.lang.model.util.ElementScanner6;

//Mark Schelkoph
//Assignment 4

class Account implements Comparable<Account>
{
  private double balance;

  Account (double b)
  {
    balance = b;
  }

  public double getBalance()
  {
    return balance;
  }

  public void setBalance(double x)
  {
    balance = x;
  }

  public void deposit(double x)
  {
    setBalance(getBalance() + x);
  }

  public void withdraw(double x)
  {
    setBalance(getBalance() - x);
  }

  public int compareTo(Account a)
  {
    if (getBalance() == a.getBalance())
    {
      return 0;
    }
    else if (getBalance() > a.getBalance())
    {
      return 1;
    }
    else
    return -1;
  }
}
