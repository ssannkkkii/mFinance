import React, { useState } from 'react';
import classes from './../MainPage.module.scss';

const Header = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(prev => !prev);
  };

  const closeMenu = () => {
    setMenuOpen(false);
  };

  return (
    <header className={classes.header}>
      <div className={classes.container}>
        <div className={classes.header__row}>
          <div className={classes.header__logo}>
            MFinance
          </div>

          <button className={`${classes.burger} ${menuOpen ? classes.open : ''}`} onClick={toggleMenu}>
            <span></span>
            <span></span>
            <span></span>
          </button>

          <nav className={`${classes.header__nav} ${menuOpen ? classes.open : ''}`}>
            <div className={classes.header__nav__link}>
              <a href="#" onClick={closeMenu}>Log in</a>
            </div>
            <div className={classes.header__nav__btn}>
              <a href="#" className={classes.button} onClick={closeMenu}>Get started</a>
            </div>
          </nav>
        </div>
      </div>

      {menuOpen && <div className={classes.overlay} onClick={closeMenu}></div>}
    </header>
  );
};

export default Header;
