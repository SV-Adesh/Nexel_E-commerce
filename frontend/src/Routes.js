import React from 'react';
import { Routes as RouterRoutes, Route, useLocation } from 'react-router-dom';
import { motion } from 'framer-motion';
import ProductList from './components/ProductList';
import Cart from './components/Cart';
import Login from './components/Login';
import Register from './components/Register';
import Profile from './components/Profile';
import Orders from './components/Orders';
import AdminDashboard from './components/AdminDashboard';

const pageVariants = {
  initial: {
    opacity: 0,
    x: -20,
  },
  animate: {
    opacity: 1,
    x: 0,
    transition: {
      duration: 0.4,
      ease: 'easeInOut',
    },
  },
  exit: {
    opacity: 0,
    x: 20,
    transition: {
      duration: 0.3,
    },
  },
};

const PageWrapper = ({ children }) => (
  <motion.div
    variants={pageVariants}
    initial="initial"
    animate="animate"
    exit="exit"
  >
    {children}
  </motion.div>
);

const Routes = () => {
  const location = useLocation();

  return (
    <RouterRoutes location={location} key={location.pathname}>
      <Route
        path="/"
        element={
          <PageWrapper>
            <ProductList />
          </PageWrapper>
        }
      />
      <Route
        path="/products"
        element={
          <PageWrapper>
            <ProductList />
          </PageWrapper>
        }
      />
      <Route
        path="/cart"
        element={
          <PageWrapper>
            <Cart />
          </PageWrapper>
        }
      />
      <Route
        path="/login"
        element={
          <PageWrapper>
            <Login />
          </PageWrapper>
        }
      />
      <Route
        path="/register"
        element={
          <PageWrapper>
            <Register />
          </PageWrapper>
        }
      />
      <Route
        path="/profile"
        element={
          <PageWrapper>
            <Profile />
          </PageWrapper>
        }
      />
      <Route
        path="/orders"
        element={
          <PageWrapper>
            <Orders />
          </PageWrapper>
        }
      />
      <Route
        path="/admin"
        element={
          <PageWrapper>
            <AdminDashboard />
          </PageWrapper>
        }
      />
    </RouterRoutes>
  );
};

export default Routes; 