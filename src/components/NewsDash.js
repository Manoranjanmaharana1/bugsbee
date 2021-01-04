import React, { useEffect, useState } from 'react';
import NewsCard from './NewsCard';
import Firebase from 'firebase/app';
import 'firebase/database';

const NewsDash = () => {
    const [data, setData] = useState([]);
    
    function shuffle(array) {
        array.sort(() => Math.random() - 0.5);
      }
    useEffect(() => {
        let ls = [];
        const firebaseConfig = {
            apiKey: "AIzaSyCBhndH3lTBDn0AcmTbPkxMRpWHJqaG6Y0",
            authDomain: "technews-875b3.firebaseapp.com",
            databaseURL: "https://technews-875b3-default-rtdb.firebaseio.com",
            projectId: "technews-875b3",
            storageBucket: "technews-875b3.appspot.com",
            messagingSenderId: "179620553857",
            appId: "1:179620553857:web:c0fda7ddff559dcfbb5980"
        };
        !Firebase.apps.length ? Firebase.initializeApp(firebaseConfig) : Firebase.app()
        Firebase.database().ref('/').once('value').then((snapshot) => {
                snapshot.forEach((children) => {
                    
                   //ls.push(children.toJSON()); 
                   children.forEach((child) => {
                    
                    ls.push(child.toJSON()); 
                    
                 });
                });
                shuffle(ls);
                setData(ls);    
            });
            
    }, []);
    return (
        <div className="container">
        <div className="dash-container">
            {data.map((item, idx) => (
                <NewsCard Date={item._News__timestamp} Heading={item._News__headline} Img={item._News__imgURL} URL={item._News__sourceURL} key={idx} />
            ))}
        </div>
        </div>
    )
}
export default NewsDash;