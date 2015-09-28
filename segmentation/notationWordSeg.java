
public enum notationWordSeg {
	SINGLE ("S"),
 	BEGIN ("B"),
	INSIDE ("I");
	
    private final String sign;   // notation sign

    notationWordSeg(String sign){
    	this.sign = sign;
    }

    public String getSign() {
        return this.sign;
    }

}
