package com.example.app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;

import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

public class Check extends AppCompatActivity {
    FirebaseAuth auth;
    FirebaseUser user;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        auth = FirebaseAuth.getInstance();
        super.onCreate(savedInstanceState);
        if (auth.getCurrentUser() != null) {
            login();
            finish(); //mora
            //startActivity(new Intent(this, MainActivity.class));
        } else {
            finish(); //mora
            startActivity(new Intent(this, Login.class));
        }
    }

    void login() {
        FirebaseFirestore db = FirebaseFirestore.getInstance();
        //auth = FirebaseAuth.getInstance();
        user = auth.getCurrentUser();

        CollectionReference colRef = db.collection("Users");
        colRef.get().addOnSuccessListener(new OnSuccessListener<QuerySnapshot>() {
            @Override
            public void onSuccess(QuerySnapshot queryDocumentSnapshots) {
                for (QueryDocumentSnapshot doc : queryDocumentSnapshots) {
                    String ID = doc.getString("ID");
                    if (doc.getString("ID").equals(user.getUid())) {
                        finish();
                        System.out.println("Ima ih " + user.getUid());
                        Intent i = new Intent(Check.this, MainActivity.class);
                        i.putExtra("Tip", doc.getString("Type"));
                        startActivity(i);
                        //startActivity(new Intent(Check.this, Login.class));
                    }
                }
            }
        });
    }
}