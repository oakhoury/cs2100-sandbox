import java.util.Scanner;

class GreetGeneration {

    /**
     * Maps a numeric year to the generation name for that birth year
     * @param year the yeart to be mapped to its generation
     * @return one of the named Generation values, e.g.: Baby Boomers
     */
  public static String getGeneration(int year) {
    String generation;

    if (year < 1901)
      generation = "Unknown";
    else if (year <= 1927)
        generation = "Greatest Generation";
    else if (year <= 1945)
        generation = "Silent Generation";
    else if (year <= 1964)
        generation = "Baby Boomers";
    else if (year <= 1980)
        generation = "Generation X";
    else if (year <= 1996)
        generation = "Millenials";
    else if (year <= 2012)
        generation = "Generation Z (\"Zoomers\")";
    else
        generation = "Generation Alpha";

    return generation;
    
  }

  public static void main(String[] params) {
    Scanner userInputScanner = new Scanner(System.in);

    System.out.print("What is your name: ");
    String name = userInputScanner.nextLine();

    System.out.print("What is your birth year: ");
    int year = userInputScanner.nextInt();

    String generation = getGeneration(year);

    System.out.printf("Great to meet you %s, you are in the %s!\n", name, generation);
  }
}
