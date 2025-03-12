import { createTheme } from '@mui/material/styles';

export const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#00a0ff',
      light: '#33b4ff',
      dark: '#0070b3',
    },
    secondary: {
      main: '#ff3d00',
      light: '#ff6333',
      dark: '#b22a00',
    },
    background: {
      default: '#121212',
      paper: 'rgba(31, 31, 31, 0.8)',
    },
    text: {
      primary: '#ffffff',
      secondary: 'rgba(255, 255, 255, 0.7)',
    },
    divider: 'rgba(255, 255, 255, 0.12)',
  },
  components: {
    MuiPaper: {
      styleOverrides: {
        root: {
          backdropFilter: 'blur(10px)',
          backgroundColor: 'rgba(31, 31, 31, 0.8)',
          boxShadow: '0 8px 32px 0 rgba(0, 0, 0, 0.37)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          transition: 'all 0.3s ease-in-out',
          '&:hover': {
            boxShadow: '0 12px 40px 0 rgba(0, 0, 0, 0.5)',
            backgroundColor: 'rgba(41, 41, 41, 0.9)',
          },
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          background: 'linear-gradient(145deg, rgba(41, 41, 41, 0.9), rgba(31, 31, 31, 0.8))',
          transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
          '&:hover': {
            transform: 'translateY(-8px) scale(1.02)',
            boxShadow: '0 20px 40px rgba(0, 0, 0, 0.5)',
            '& .MuiCardMedia-root': {
              transform: 'scale(1.1)',
            },
          },
          '& .MuiCardMedia-root': {
            transition: 'transform 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
          },
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: '25px',
          textTransform: 'none',
          fontWeight: 600,
          transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
          background: 'linear-gradient(45deg, #00a0ff 30%, #00e5ff 90%)',
          '&:hover': {
            transform: 'scale(1.05)',
            background: 'linear-gradient(45deg, #00e5ff 30%, #00a0ff 90%)',
            boxShadow: '0 6px 20px rgba(0, 160, 255, 0.4)',
          },
        },
        contained: {
          boxShadow: '0 4px 15px rgba(0, 160, 255, 0.2)',
        },
      },
    },
    MuiAppBar: {
      styleOverrides: {
        root: {
          background: 'rgba(18, 18, 18, 0.8)',
          backdropFilter: 'blur(10px)',
          boxShadow: '0 4px 20px rgba(0, 0, 0, 0.15)',
        },
      },
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          '& .MuiOutlinedInput-root': {
            transition: 'all 0.3s ease-in-out',
            '&:hover': {
              '& fieldset': {
                borderColor: '#00a0ff',
              },
            },
            '&.Mui-focused': {
              '& fieldset': {
                borderColor: '#00a0ff',
                borderWidth: '2px',
              },
            },
          },
        },
      },
    },
  },
  shape: {
    borderRadius: 12,
  },
  typography: {
    fontFamily: '"Inter", "Helvetica", "Arial", sans-serif',
    h1: {
      fontWeight: 700,
      background: 'linear-gradient(45deg, #00a0ff, #00e5ff)',
      WebkitBackgroundClip: 'text',
      WebkitTextFillColor: 'transparent',
    },
    h2: {
      fontWeight: 700,
      background: 'linear-gradient(45deg, #00a0ff, #00e5ff)',
      WebkitBackgroundClip: 'text',
      WebkitTextFillColor: 'transparent',
    },
    h3: {
      fontWeight: 600,
    },
    h4: {
      fontWeight: 600,
    },
    h5: {
      fontWeight: 500,
    },
    h6: {
      fontWeight: 500,
    },
  },
}); 