package com.example.app;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

import java.util.HashMap;
import java.util.Map;

public class User_data extends AppCompatActivity {
    EditText e;
    EditText p;
    EditText n;
    Button b;
    FirebaseAuth auth;
    FirebaseUser user;
    int a = 0;
    int c = 0;
    String name;
    String email;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_data);

        b = findViewById(R.id.button3);
        e = findViewById(R.id.editTextTextEmailAddress3);
        p = findViewById(R.id.editTextTextPassword3);
        n = findViewById(R.id.editTextTextPersonName2);
        auth = FirebaseAuth.getInstance();

        Intent intent = getIntent();
        email = intent.getStringExtra("E-mail");
        name = intent.getStringExtra("Ime");
        String ID = intent.getStringExtra("ID");
        String tip = intent.getStringExtra("Tip");
        e.setText(email);
        n.setText(name);

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                e = findViewById(R.id.editTextTextEmailAddress3);
                p = findViewById(R.id.editTextTextPassword3);
                n = findViewById(R.id.editTextTextPersonName2);
                if (!email.equals(e.getText().toString()) || !name.equals(n.getText().toString())) a++;
                if (!p.getText().toString().equals("")) a++;
                if  (!email.equals(e.getText().toString()) || !name.equals(n.getText().toString()) || !p.getText().toString().equals("")) {
                    if (!p.getText().toString().equals("")) {
                        auth = FirebaseAuth.getInstance();
                        user = auth.getCurrentUser();
                        user.updatePassword(p.getText().toString()).addOnSuccessListener(new OnSuccessListener<Void>() {
                            @Override
                            public void onSuccess(Void aVoid) {
                                c++;
                                poruka();
                            }
                        });
                    }
                    if (!name.equals(n.getText().toString()) || !email.equals(e.getText().toString())) {
                        user = auth.getCurrentUser();
                        name = n.getText().toString();
                        email = e.getText().toString();
                        Map<String, Object> u = new HashMap<>();
                        u.put("Full name", name);
                        u.put("E-mail", email);
                        u.put("ID", user.getUid());
                        u.put("Type", tip);
                        FirebaseFirestore db = FirebaseFirestore.getInstance();

                        CollectionReference colRef = db.collection("Users");
                        colRef.document(ID).update(u).addOnCompleteListener(new OnCompleteListener<Void>() {
                            @Override
                            public void onComplete(@NonNull Task<Void> task) {
                                if (task.isSuccessful()) {
                                    c++;
                                    poruka();
                                } else {
                                    Toast.makeText(User_data.this, task.getException().toString(), Toast.LENGTH_SHORT).show();
                                }
                            }
                        });
                    }
                }
            }
        });
    }

    void poruka() {
        if (a == c) {
            Toast.makeText(User_data.this, "Spremljeno", Toast.LENGTH_SHORT).show();

        }
    }
}