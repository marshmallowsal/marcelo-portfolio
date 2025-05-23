# Formula Font Setup Instructions

## Getting the Formula Font (Free Alternative to Toyota Type)

The Formula font is perfect for your GAZOO Racing website as it's specifically designed with racing aesthetics in mind.

### Option 1: Formula Font (Recommended)
1. Visit: https://pangrampangram.com/products/formula
2. Click "Try for Free" 
3. Enter your email to get the free trial fonts
4. Download the following weights and place them in this `static/fonts/` directory:
   - `Formula-Light.woff2` (300 weight)
   - `Formula-Regular.woff2` (400 weight) 
   - `Formula-Medium.woff2` (500 weight)
   - `Formula-Semibold.woff2` (600 weight)
   - `Formula-Bold.woff2` (700 weight)
   - `Formula-Black.woff2` (900 weight)

### Option 2: Already Using Google Fonts Fallbacks
If you can't get the Formula font, the CSS already includes these free Google Fonts as fallbacks:
- **Inter** - Modern, highly legible
- **Poppins** - Geometric, perfect for tech/automotive
- **Montserrat** - Clean, modern design

### Current Font Stack
```css
font-family: 'Formula', 'Inter', 'Poppins', 'Montserrat', 'Segoe UI', Roboto, Arial, sans-serif;
```

The browser will automatically use the first available font in the list.

### File Structure
Place your Formula font files here:
```
static/fonts/
├── Formula-Light.woff2
├── Formula-Regular.woff2
├── Formula-Medium.woff2
├── Formula-Semibold.woff2
├── Formula-Bold.woff2
└── Formula-Black.woff2
```

### License Notes
- Formula: Free for personal use, commercial licenses available
- Inter, Poppins, Montserrat: Completely free for all uses (Google Fonts)

The current setup ensures your site will look great regardless of whether you have Formula installed or not! 