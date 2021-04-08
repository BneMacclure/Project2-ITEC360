import java.util.*;
import java.util.regex.*;
/** A utility class for generating inputs for `closest`. 
 * Prints to stdout.
 *
 * @see https://www.radford.edu/itec360/2021spring-ibarland/Homeworks/Proj02/proj02.html#input
 * @author ibarland
 * @version 2021-mar-27
 * @license CC-BY; a URL to this original file suffices as attribution.
 *
 * Currently supports the mthds @{knownMthds}.
 * 
 * Each method for generating takes in n (#points to generate),
 * a random-number generator (may or may not be used, depending on the method),
 * plus 0 or more strings (may or may not be used, depending on the method).
 */
public class GeneratePoints{
    static List<String> knownMthds = List.of("rand","circ","test");
    static String executable = "java " + getMainClassName("GeneratePoints");

    static String USAGE =
        "Usage:\n"
        + "    " + executable + " [-s <seed>] <n> <mthd> [<other-args>…]\n"
        + "where:\n"
        + "    <n> is a number-of-points (natnum <= " + Integer.MAX_VALUE + "),\n"
        + "    <mthd> is one of " + knownMthds + "\n"
        + "    <seed> is a long to give to a random-number-generator,\n"
        + "    <other-args>… are specific to which <mthd> is used.\n"
        + "\n"
        + "Prints to stdout: lines suitable as input to `closest` (if n>=2).\n"
        + "\n"
        + "Examples:\n"
        + "    " + executable + " 10 rand" + "\n"
        + "    " + executable + "  8 circ" + "\n"
        + "    " + executable + "  4 circ 10 800 800" + "\n"
        + "\n"
        + "Supported mthds for generating points:\n"
        + "   rand: generate points randomly\n"
        + "   circ: generate points roughly in a circle; other-args: r,x,y (all optional)\n"
        ;


    public static final int MAX_COORD = 1<<30;
    // For any int/long `n`,  `n%MAX_COORD` is in [-2^30, 2^30), as per problem-spec.
    
    /** @return `n` random points (created with `ints`),
     * represented as a string per hw.
     *
     * @see https://www.radford.edu/itec360/2021spring-ibarland/Homeworks/Proj02/proj02.html#input 
     */
    static String rand( int n, Iterator<Integer> ints ) {
        StringBuilder s = new StringBuilder( 5+6*n );
        for (int i=0;  i<n;  ++i) {
            s.append( String.format("%d %d\n", ints.next()%MAX_COORD, ints.next()%MAX_COORD ) );
            }
        return s.toString();
        }
    static String rand( int n, Random rng ) { return rand( n, rng.ints(2*n).iterator() ); }

    static void testRand() {
        var natnums = new Iterator<Integer>() { private int i=0;  
                                                public Integer next() { return i++;}  
                                                public boolean hasNext() { return true; }
                                              };
        assert rand( 0,natnums).equals("");
        assert rand( 1,natnums).equals("0 1\n");
        assert rand( 2,natnums).equals("2 3\n4 5\n");
        assert rand(50,natnums).split("\n").length == 50;
        }
        /* Note: test functions should really be in their own class,
         * and use a better framerwork than mere built-in `assert`s (like JUnit).
         * But for ease of studnets only downloading one file,
         * and also maybe *looking* at the tests and seeing how to test things
         * which may not seem testable, I put tests in the same class as
         * the code-it-tests.  --ibarland
         */


    /** @return a roughly-circular set of n points (rounded to integers),
     * represented as a string per hw.
     *
     * args[0..2] can contain the radius and (x,y) center of the circle;
     * Default values are r=50.0, (x,y) = (0.0, 0.0).
     * @see https://www.radford.edu/itec360/2021spring-ibarland/Homeworks/Proj02/proj02.html#input 
     */
    static String circ( int n, String... args ) {
        double r = args.length < 1  ?  100.0  :  Double.parseDouble(args[0]);
        double x = args.length < 2  ?    0.0  :  Double.parseDouble(args[1]);
        double y = args.length < 3  ?    0.0  :  Double.parseDouble(args[2]);
        
        StringBuilder s = new StringBuilder( 5+6*n );
        for (int i=0;  i<n;  ++i) {
            double θ  = (double)i/n * (2*Math.PI);
            double Δx = x + r*Math.cos(θ);
            double Δy = y + r*Math.sin(θ);
            s.append( String.format( "%d %d\n", (int)Math.round(Δx), (int)Math.round(Δy) ) );
            }
        return s.toString();
        }


    static void testCirc() {
        assert circ(0).equals("");
        assert circ(1).equals("100 0\n");
        assert circ(2).equals("100 0\n-100 0\n");
        assert circ(4).equals("100 0\n0 100\n-100 0\n0 -100\n");
        int root3Over2 = (int)Math.round(100*Math.sqrt(3)/2);
        assert circ(3).equals(String.format("100 0\n-50 %d\n-50 %d\n", root3Over2, -root3Over2));
        }





    /**
     * This method has much more error-handling than required for student-projects
     * (but since it's being given to students to use, I try for better error messages,
     * as well as an example of how to handle such things if you need to 
     * -- which the main assignment doesn't).
     */
    public static void main( String... args ) {

        Object[] configs = getConfigsFromArgs( args, 20211L, knownMthds );  // returns: array w/ [n,mthd,otherArgs,rng]
        final int      n         =  (Integer)configs[0];
        final String   mthd      =   (String)configs[1];
        final String[] otherArgs = (String[])configs[2];
        final Random   rng       =   (Random)configs[3];
        // too bad we don't have pattern-matching to help combine the above lines into 1.

        String pts = switch(mthd) {
            case "rand" -> rand(n, rng);
            case "circ" -> circ(n, otherArgs ); 
            case "test" -> { testAll(true); System.exit(0); yield "[unreachable code?!]"; }
            default     -> "[huh? unreachable code?!]";
            };

        System.out.printf("%d\n%s", n, pts);
        }

    // No unit-tests for `main`, since it prints (and doesn't `return` -- doesn't play nice w/ test-harnesses).
    // 
    // Note that if we *could* still test functions-that-print if we could re-assign to System.out -- 
    // setting it to be a PrintStream that prints into a string-buffer (say).
    // Alas, Java declared the field `out` as `final`, oh well nevermind. 
    //
    // (Some languages *do* let you "parameterize" stdout -- php has `ob_start` for output-buffering,
    // and racket has the more general notion of `parameters`  [poor name though -- 
    // it's a v.different concept from function-params.  More like dynamic scope, to effect global variables.)


    /** Figure out `n` and `mthd` (and the rng), from the command-line args. 
     *  @return an array w/ exactly 4 items: n, mthd, mthd-args, rng
     * This method will printUsageAndExit(), if bad arguments.
     */
    static Object[] getConfigsFromArgs( String[] args, long defaultSeed, List<String> knownMthds ) {
        int n = -999;
        String mthd;
        Random rng = new Random( defaultSeed );
        int argi = 0; // the index of the arg we're processing

        dprintf( "args is: %s", Arrays.toString(args) );
        if (argi >= args.length) printUsageAndExit(-1,"no arguments provided"); 

        // check for two special arguments:
        if (Pattern.matches( "-*(?i)help", args[0] )) printUsageAndExit(0); 
        if (Pattern.matches( "-*(?i)test", args[0] )) return new Object[]{n,"test",new String[0],rng};

        // process args to set the rng seed:
        if (Pattern.matches( "-s|--seed", args[argi])) {
            ++argi;
            if (argi >= args.length) printUsageAndExit(-2,"must provide seed after '%s'", args[argi-1]);
            try { rng.setSeed( Long.parseLong(args[argi]) ); }
            catch (NumberFormatException e) { printUsageAndExit(-2,"seed must be a long-integer (got '%s')", args[argi]); }
            ++argi;
            }
        
        // process args to find n
        if (argi >= args.length) printUsageAndExit(-3, "must provide n (#points)" );
        try { n = Integer.parseInt(args[argi]); }
        catch (NumberFormatException e) { printUsageAndExit(-3,"n must be an integer (got '%s')", args[argi]); }
        ++argi;

        // process args to find mthd, and call it!
        if (argi >= args.length) printUsageAndExit(-4, "no mthd selected; must be one of %s", knownMthds );
        mthd = args[argi];
        if (!knownMthds.contains(mthd)) printUsageAndExit(-4,"mthd must be one of %s (got '%s')", knownMthds, mthd );
        ++argi;

        return new Object[]{ n, mthd, Arrays.copyOfRange(args,argi,args.length), rng };
        }
    
    static void testGetConfigsFromArgs() {
        // we ONLY test "succesful" inputs, since otherwise `getConfigsFromArgs` System.exit()s, 
        // which is particularly harsh for test-harnesses. 
        Object[] actual;   //  actual will contains 4 Objects: n,mthd,mthdArgs,rng
        Random expectedRng;

        actual = getConfigsFromArgs( new String[]{ "50", "actCool"},  22L,  List.of("actCool","actDorky","sitTight") );
        assert (int)(Integer)actual[0] == 50;
        assert actual[1].equals("actCool");
        assert Arrays.deepEquals( (String[])actual[2], new String[]{} );
        assert ((Random)actual[3]).nextInt() == (new Random(22L)).nextInt();

        // check "-s"
        actual = getConfigsFromArgs( new String[]{ "-s", "99", "50", "actCool"},  22L,  List.of("actCool","actDorky","sitTight") );
        assert (int)(Integer)actual[0] == 50;
        assert actual[1].equals("actCool");
        assert Arrays.deepEquals( (String[])actual[2], new String[]{} );
        assert ((Random)actual[3]).nextInt() == (new Random(99)).nextInt();

        // check "--seed"
        actual = getConfigsFromArgs( new String[]{ "--seed", "99", "50", "actCool"},  22L,  List.of("actCool","actDorky","sitTight") );
        assert (int)(Integer)actual[0] == 50;
        assert actual[1].equals("actCool");
        assert Arrays.deepEquals( (String[])actual[2], new String[]{} );
        assert ((Random)actual[3]).nextInt() == (new Random(99)).nextInt();

        // check add'l args
        actual = getConfigsFromArgs( new String[]{ "44", "actDorky", "extra-arg-1", "extra-arg-2"},  22L,  List.of("actCool","actDorky","sitTight") );
        assert (int)(Integer)actual[0] == 44;
        assert actual[1].equals("actDorky");
        assert Arrays.deepEquals( (String[])actual[2], new String[]{"extra-arg-1","extra-arg-2"} );
        assert ((Random)actual[3]).nextInt() == (new Random(22L)).nextInt();

        }


    public static void testAll( boolean verbose ) {
        verifyAssertionsEnabled();
        testGetConfigsFromArgs();
        testRand();
        testCirc();
        if (verbose) System.err.printf("(tests complete)\n"); 
        }
    public static void testAll() { testAll(false); }


    static void printUsageAndExit( int exitCode, String extraInfoFormat, Object... extraInfo ) {
        if (extraInfoFormat != null) System.err.printf("illegal option: " + extraInfoFormat+"\n\n", extraInfo);
        System.err.println(USAGE);
        System.exit(exitCode);
        }
    static void printUsageAndExit(int exitCode) { printUsageAndExit(exitCode, null); }

    static void dprintf( String fmt, Object... itms ) { System.err.printf(fmt+"\n", itms);
                                                      }

    /** Throw an error, if we are running w/o -enableassertions.
     *
     * (Note: assertions can be enabled on a per-class basis, so just because they're
     *  enabled in this class we can't assume they're enabled in other classes.
     *  …So the following function needs to be re-copy/pasted into any class that wants to use it!)
     */
    static void verifyAssertionsEnabled() {
        boolean exceptionRaised = false;
        try { assert false; }
        catch (AssertionError e) { exceptionRaised = true; }
        
        if (!exceptionRaised) 
            throw new AssertionError( "Assertions not enabled;\nRe-run jvm with `java -enableassertions …`."); 
        }
    
    
    /** @return the name of the starting-class/executable 
     *  Return `fallback` if somehow the stack trace is empty.
     *  (Works for single-threaded programs.)
     *  @see https://stackoverflow.com/a/36949543/320830 (thanks, Dave of stackoverflow)
     */
    public static String getMainClassName(String fallback) {
        StackTraceElement[] trace = Thread.currentThread().getStackTrace();
        return (trace.length > 0)  ?  trace[trace.length-1].getClassName()  :  fallback;
        }
    public static String getMainClassName() { return getMainClassName("[unknown]"); }

    }
