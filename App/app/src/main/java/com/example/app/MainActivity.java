package com.example.app;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

public class MainActivity extends AppCompatActivity {
    FirebaseAuth auth;
    FirebaseUser user;
    String tip;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        auth = FirebaseAuth.getInstance();
        /*user = auth.getCurrentUser();
        FirebaseFirestore db = FirebaseFirestore.getInstance();

        CollectionReference colRef = db.collection("Users");
        colRef.get().addOnSuccessListener(new OnSuccessListener<QuerySnapshot>() {
            @Override
            public void onSuccess(QuerySnapshot queryDocumentSnapshots) {
                for (QueryDocumentSnapshot doc : queryDocumentSnapshots) {
                    String ID = doc.getString("ID");
                    String email = doc.getString("E-mail");
                    String type = doc.getString("Type");
                    if (ID.equals(user.getUid()) && type.equals("1")) {
                        t.setText(email + ", admin");
                        break;
                    } else if (ID.equals(user.getUid()) && type.equals("2")) {
                        t.setText(email + ", korisnik");
                        break;
                    }
                }
            }
        });*/

        TextView t = findViewById(R.id.textView);
        Intent intent = getIntent();
        tip = intent.getStringExtra("Tip");
        t.setText(tip);

        /*Button b = findViewById(R.id.button3);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                auth.signOut();
                finish();
                startActivity(new Intent(MainActivity.this, Login.class));
            }
        });*/
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        if (tip.equals("1")) {
            inflater.inflate(R.menu.menu_admin, menu);
        } else {
            inflater.inflate(R.menu.menu, menu);
        }
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle item selection
        switch (item.getItemId()) {
            case R.id.user_data:
                user = auth.getCurrentUser();
                FirebaseFirestore db = FirebaseFirestore.getInstance();

                CollectionReference colRef = db.collection("Users");
                colRef.get().addOnSuccessListener(new OnSuccessListener<QuerySnapshot>() {
                    @Override
                    public void onSuccess(QuerySnapshot queryDocumentSnapshots) {
                        for (QueryDocumentSnapshot doc : queryDocumentSnapshots) {
                            if (doc.getString("ID").equals(user.getUid())) {
                                finish();
                                String name = doc.getString("Full name");
                                String email = doc.getString("E-mail");
                                String ID = doc.getId();
                                Intent i = new Intent(MainActivity.this, User_data.class);
                                i.putExtra("Ime", name);
                                i.putExtra("E-mail", email);
                                i.putExtra("ID", ID);
                                i.putExtra("Tip", tip);
                                startActivity(i);
                                break;
                                //startActivity(new Intent(Check.this, Login.class));
                            }
                        }
                    }
                });
                return true;
            case R.id.add_admin:
                finish();
                Intent i = new Intent(MainActivity.this, Register.class);
                i.putExtra("Tip", "1");
                startActivity(i);
                return true;
            case R.id.sign_out:
                auth.signOut();
                finish();
                startActivity(new Intent(MainActivity.this, Login.class));
                return true;

            default:
                return super.onOptionsItemSelected(item);
        }
    }
}