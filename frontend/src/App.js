import Footer from './pages/Footer/Footer';
import Header from './pages/Header/Header';
import AppRouter from './utils/router';

const App = () => {
  return (
    <>
      <Header />
      <AppRouter />
      <Footer />
    </>
  );
};

export default App;
