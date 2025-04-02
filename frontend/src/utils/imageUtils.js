/**
 * Ensures an image URL is properly formatted with the backend server URL if needed
 * @param {string} imageUrl - The image URL from the API
 * @returns {string} - The properly formatted image URL
 */
export const getFullImageUrl = (imageUrl) => {
  // Handle null, undefined, or empty strings
  if (!imageUrl || imageUrl === '') {
    return 'https://via.placeholder.com/600x400/2c3e50/ffffff?text=No+Image+Available';
  }
  
  // Handle already fully-qualified URLs
  if (imageUrl.startsWith('http')) {
    return imageUrl;
  }
  
  // Handle non-slash prefixed paths
  if (!imageUrl.startsWith('/')) {
    imageUrl = '/' + imageUrl;
  }
  
  // Add backend server URL to relative path
  return `http://localhost:8000${imageUrl}`;
}; 