import React from 'react';


const Hero = () => {




    return (
        <div className="hero-container">
            <div className="top-hero">
                <img src="./images/heroImg.png" className="top-img" alt="" />
            </div>
            <div className="top-button">
                <h1>Start Exploring Digital World</h1>
            </div>
            <div className="content-box">
                <div className="content-row1">
                    <div className="row1-left">
                    <h1>Intimidate by the new inventions.</h1>   
                    </div>
                    <div className="row1-right">
                        <img src="./images/techMeeting.jpg" alt="" />
                    </div>
                </div>
                <div className="content-row2">
                    <div className="row2-left">
                    <img src="./images/techFest.jpg" alt="" />
                    </div>
                    <div className="row2-right">
                    <h1>Learn how and what digital market are changing.</h1>
                    </div>
                </div>
                <div className="content-row1">
                    <div className="row1-left">
                    <h1>Explore trending tech and its scope with no limits.</h1>
                    </div>
                    <div className="row1-right">
                    <img src="./images/multiplebooks.jpg" alt="" />
                    </div>
                </div>
            </div>
            <div className="bottom-hero">
                <div className="bottom-shape">
                    <h1>Know every aspect of new technology emerging everyday.</h1>
                </div>
                <img src="./images/hololens.png" alt="" className="bottom-img"/>
            </div>
            <div className="footer">
                
            </div>
        </div>
    )
}



export default Hero;