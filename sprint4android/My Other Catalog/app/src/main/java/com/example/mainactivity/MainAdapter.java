package com.example.mainactivity;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class MainAdapter extends RecyclerView.Adapter <MainViewHolder>{
    private List <AnimalData> allTheData;
    private Activity activity;



    public MainAdapter(List<AnimalData> dataSet, Activity activity){
        this.allTheData=dataSet;
        this.activity =activity;
    }

    public MainViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.animal_view_holder,parent,false);
        return new MainViewHolder(view);
    }


    public void onBindViewHolder(MainViewHolder holder, int position) {
        AnimalData dataInPositionToBeRendered = allTheData.get(position);
        holder.showData(dataInPositionToBeRendered,activity);

    }

    public int getItemCount() {
        return allTheData.size();
    }
}
