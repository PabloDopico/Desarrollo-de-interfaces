package com.example.mainactivity;

import org.json.JSONException;
import org.json.JSONObject;

public class AnimalData {

    private String name;
    private String imageUrl;

    public AnimalData(JSONObject json) {
        try{
            this.name=json.getString("name");
            this.imageUrl=json.getString("image_url");
        }catch (JSONException error){
            error.printStackTrace();
        }

    }

    public String getName(){ return name; }

    public String getImageUrl(){ return imageUrl; }
}
