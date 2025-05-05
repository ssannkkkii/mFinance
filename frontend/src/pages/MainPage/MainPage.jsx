import React from 'react';
import classes from './MainPage.module.scss';
import Header from './Header/Header';
import Footer from './Footer/Footer';

import image1 from './../../images/first_image.svg'
import image2 from './../../images/second_image.svg'
import image3 from './../../images/last_image.svg'


const MainPage = () => {
  return (
    <div>
      <Header/>
      <main>
        <div className={classes.home}>
          
          
          <div className={classes.home__block}>
            <div className={classes.container}>
              <div className={classes.home__block__row}>
                <div className={classes.home__block__content}>
                  <h1>Start to manage your finance right now!</h1>
                  <p>
                    Knowing your income and expenses will help you make
                    informed financial decisions and achieve your goals.
                  </p>
                  <div className={classes.home__block__buttons}>
                    <a href="#" className={classes.button}>
                      Start manage
                      <svg width="30" height="16" viewBox="0 0 30 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                          d="M29.7071 8.70711C30.0976 8.31659 30.0976 7.68342 29.7071 7.2929L23.3431 0.928934C22.9526 0.53841 22.3195 0.53841 21.9289 0.928934C21.5384 1.31946 21.5384 1.95262 21.9289 2.34315L27.5858 8L21.9289 13.6569C21.5384 14.0474 21.5384 14.6805 21.9289 15.0711C22.3195 15.4616 22.9526 15.4616 23.3431 15.0711L29.7071 8.70711ZM-8.74228e-08 9L29 9L29 7L8.74228e-08 7L-8.74228e-08 9Z"
                          fill="white" />
                      </svg>
                    </a>
                    <a href="#" className={classes.link}>Log in</a>
                  </div>
                </div>
                <div className={classes.home__block__image}>
                  <img src={image1}/>
                </div>
              </div>
            </div>
          </div>

          <div className={classes.home__block}>
            <div className={classes.container}>
            <div className={`${classes.home__block__row} ${classes.reverse}`}>
                <div className={classes.home__block__content}>
                  <h2>Control over finances is the key to success</h2>
                  <p>
                    By saving money, you can find a key to solving problems
                    or helping someone else
                  </p>
                  <ul>
                    <li>Productive saving money</li>
                    <li>Becoming a financially literate person</li>
                  </ul>
                </div>
                <div className={classes.home__block__image}>
                  <img src={image2}/>
                </div>
              </div>
            </div>
          </div>
          
          <div className={classes.home__block}>
            <div className={classes.container}>
              <div className={classes.home__block__row}>
                <div className={classes.home__block__content}>
                  <h1>Therefore, it is necessary to focus on managing your
                  finances</h1>
                  <p>
                    With the help of the right strategy and planning, you
                    can achieve great success in personal finance
                  </p>
                  <div className={classes.home__block__buttons}>
                    <a href="#" className={classes.button}>
                      Start manage
                      <svg width="30" height="16" viewBox="0 0 30 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                          d="M29.7071 8.70711C30.0976 8.31659 30.0976 7.68342 29.7071 7.2929L23.3431 0.928934C22.9526 0.53841 22.3195 0.53841 21.9289 0.928934C21.5384 1.31946 21.5384 1.95262 21.9289 2.34315L27.5858 8L21.9289 13.6569C21.5384 14.0474 21.5384 14.6805 21.9289 15.0711C22.3195 15.4616 22.9526 15.4616 23.3431 15.0711L29.7071 8.70711ZM-8.74228e-08 9L29 9L29 7L8.74228e-08 7L-8.74228e-08 9Z"
                          fill="white" />
                      </svg>
                    </a>
                  </div>
                </div>
                <div className={classes.home__block__image}>
                  <img src={image3}/>
                </div>
              </div>
            </div>
          </div>


        </div>
      </main>
      <Footer/>
    </div>
  );
};

export default MainPage;