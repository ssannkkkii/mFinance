import React from 'react';
import classes from './../MainPage/MainPage.module.scss';
import '@fortawesome/fontawesome-free/css/all.min.css';

const Footer = () => {
  return (
    <footer className={classes.footer}>
      <div className={classes.container}>
        <div className={classes.footer__row}>
          <div className={classes.footer__column}>
            <h3 className={classes.footer__logo}>
              <span className={classes.green}>M</span>Finance
            </h3>
            <p className={classes.footer__desc}>
              Solution of managing <br />
              and saving your money
            </p>
          </div>
          <div className={classes.footer__column}>
            <h4>Company</h4>
            <ul>
              <li><a href="#">About us</a></li>
              <li><a href="#">Teems of Servise</a></li>
              <li><a href="#">Priacy Policy</a></li>
            </ul>
          </div>
          <div className={classes.footer__column}>
            <h4>Subscribe on our news</h4>
            <div className={classes.footer__subscribe}>
              <input type="email" placeholder="Enter your E-mail.." />
              <button>Subscribe</button>
            </div>
            <div className={classes.footer__socials}>
              <i className="fab fa-facebook-f"></i>
              <i className="fab fa-instagram"></i>
              <i className="fab fa-twitter"></i>
              <i className="fab fa-youtube"></i>
            </div>
          </div>
        </div>
        <div className={classes.footer__bottom}>
          <p>© 2023 All rights reserved</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
