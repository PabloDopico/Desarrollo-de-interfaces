package com.example.mainactivity;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;

public class MainViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;

    public MainViewHolder(@NonNull View itemView){
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.animal_name_text_view);
        imageView= (ImageView) itemView.findViewById(R.id.animal_image_view);
    }

    public void showData(AnimalData data, Activity activity){
        textView.setText(data.getName());
        loadImage(data.getImageUrl(), activity);
    }


    private void loadImage(String imageUrl, Activity activity) {

        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                Bitmap image = getBitmapFromUrl(imageUrl);
                activity.runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        imageView.setImageBitmap(image);
                    }
                });
            }
        });
        thread.start();
    }

    private Bitmap getBitmapFromUrl(String urlString) {
        try {
            URL url = new URL(urlString);
            URLConnection connection = (URLConnection) url.openConnection();
            connection.setDoInput(true);
            connection.connect();
            InputStream input = connection.getInputStream();
            Bitmap resultBitmap = BitmapFactory.decodeStream(input);
            return resultBitmap;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
}
