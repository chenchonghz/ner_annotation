
public enum notationDict {
	OutOfV ("OV"),
 	BEGIN ("BV"),
	INSIDE ("IV");
	
    private final String sign;   // notation sign

    notationDict(String sign){
    	this.sign = sign;
    }

    public String getSign() {
        return this.sign;
    }

}
