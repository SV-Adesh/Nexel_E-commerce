import React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  IconButton,
  Badge,
  Box,
} from '@mui/material';
import {
  ShoppingCart as CartIcon,
  Person as PersonIcon,
  AdminPanelSettings as AdminIcon,
} from '@mui/icons-material';
import { useAuth } from '../contexts/AuthContext';
import { useCart } from '../contexts/CartContext';

const Navbar = () => {
  const { user, logout } = useAuth();
  const { getCartItemCount } = useCart();

  const handleAdminClick = () => {
    window.open('http://localhost:8000/admin/', '_blank');
  };

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography
          variant="h6"
          component={RouterLink}
          to="/"
          sx={{
            flexGrow: 1,
            textDecoration: 'none',
            color: 'inherit',
          }}
        >
          E-Commerce Store
        </Typography>

        <Box sx={{ display: 'flex', alignItems: 'center' }}>
          <Button
            color="inherit"
            component={RouterLink}
            to="/products"
          >
            Products
          </Button>

          <IconButton
            color="inherit"
            component={RouterLink}
            to="/cart"
            sx={{ ml: 1 }}
          >
            <Badge badgeContent={getCartItemCount()} color="error">
              <CartIcon />
            </Badge>
          </IconButton>

          {user ? (
            <>
              <Button
                color="inherit"
                component={RouterLink}
                to="/orders"
                sx={{ ml: 1 }}
              >
                Orders
              </Button>
              <IconButton
                color="inherit"
                component={RouterLink}
                to="/profile"
                sx={{ ml: 1 }}
              >
                <PersonIcon />
              </IconButton>
              <Button
                color="inherit"
                onClick={logout}
                sx={{ ml: 1 }}
              >
                Logout
              </Button>
              <Button
                color="inherit"
                onClick={handleAdminClick}
                startIcon={<AdminIcon />}
                sx={{ ml: 1 }}
              >
                Admin
              </Button>
            </>
          ) : (
            <>
              <Button
                color="inherit"
                component={RouterLink}
                to="/login"
                sx={{ ml: 1 }}
              >
                Login
              </Button>
              <Button
                color="inherit"
                component={RouterLink}
                to="/register"
                sx={{ ml: 1 }}
              >
                Register
              </Button>
            </>
          )}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar; 