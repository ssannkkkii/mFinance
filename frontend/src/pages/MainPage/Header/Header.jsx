import React from 'react';
import classes from './../MainPage.module.scss';

const Header = () => {
  return (
    <header className={classes.header}>
      <div className={classes.container}>
        <div className={classes.header__row}>
          <div className={classes.header__logo}>
            <p>MFinance</p>
            </div>
          <div className={classes.header__nav}>
            <div className={classes.header__nav__link}>
              <a href="#" className={classes.login}>Log in</a>
            </div>
            <div className={classes.header__nav__btn}>
              <a href="#" className={classes.button}>Get started</a>
            </div>
          </div>
        </div>
      </div>
	  </header>
  );
};

export default Header;