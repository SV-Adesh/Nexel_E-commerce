import React from 'react';
import { Box, Container } from '@mui/material';
import { motion } from 'framer-motion';
import Navbar from './Navbar';

const Layout = ({ children }) => {
  return (
    <Box
      sx={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        background: 'linear-gradient(135deg, #121212 0%, #1a1a1a 100%)',
        backgroundAttachment: 'fixed',
      }}
    >
      <Navbar />
      <Container
        component={motion.main}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -20 }}
        transition={{ duration: 0.3 }}
        maxWidth="lg"
        sx={{
          flex: 1,
          py: 4,
          mt: 8,
          position: 'relative',
          '&::before': {
            content: '""',
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: 'radial-gradient(circle at 50% 0%, rgba(0, 160, 255, 0.1) 0%, transparent 70%)',
            pointerEvents: 'none',
          },
        }}
      >
        {children}
      </Container>
    </Box>
  );
};

export default Layout; 