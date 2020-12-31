//Mark Schelkoph
//Assignment 2

import java.util.Scanner;

import javax.lang.model.util.ElementScanner6;

class Main {
  public static void main(String[] args) {

    boolean test = false;
    int arraySize = 5;
    String[] str = new String[arraySize];
    Scanner input = new Scanner(System.in);
    
    PasswordGenerator p = new PasswordGenerator(3, "default", "default", "default", "default", "default");

    while(test == false)
    {
      System.out.println("Enter " + arraySize + " Phrase words: ");
      String word = input.nextLine();

      String wordArray[] = word.split(" ");

      if (wordArray.length > arraySize)
      {
        System.out.println("Phrase must be less than " + arraySize + " words.\n");
      }
      else if (wordArray.length < arraySize)
      {
        System.out.println("Phrase must be at least " + arraySize + " words.\n");
      }
      else
      {
        str = wordArray;
        test = true;
      }
    }

    p.setPhrase(str[0], str[1], str[2], str[3], str[4]);

    System.out.println("\nThe Phrase you entered is: " + p.getPhrase());

    System.out.println("\nEnter default n value: ");
    p.setN(Integer.parseInt(input.next()));

    System.out.println("\nUsing n: " + p.getN() + ",\n" + "Password length = " + p.getPasswordLength() + ": " + p.getPassword());

    while(test == true)
    {
      System.out.println("\nenter \"y\" to enter different n value. (press q to quit) ");
      
      if(input.next().equals("q"))
      {
        test = false;
      }
      else
      {
        System.out.println("\nEnter default n value: ");
        p.setN(Integer.parseInt(input.next()));

        System.out.println("\nUsing n: " + p.getN() + ",\n" + "Password length = " + p.getPasswordLength() + ": " + p.getPassword());
      }
    }

    input.close();
  }
}
