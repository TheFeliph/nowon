# Nowon - Task Management Application

Nowon is a simple task management application built with Next.js, TypeScript, and Prisma.

## Prerequisites

Before you begin, ensure you have the following installed:
- Node.js (v14 or later)
- npm (usually comes with Node.js)
- PostgreSQL (for the database)

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/thefeliph/nowon.git
   cd nowon
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   DATABASE_URL="postgresql://username:password@localhost:5432/nowon?schema=public"
   ```
   Replace `username`, `password`, and `nowon` with your PostgreSQL credentials and desired database name.

4. Set up the database:
   ```
   npx prisma db push
   ```

5. (Optional) Seed the database:
   ```
   npx prisma db seed
   ```

## Running the Application

To run the application in development mode:

```
npm run dev
```

The application will be available at `http://localhost:3000`.

## Building for Production

To build the application for production:

```
npm run build
```

To start the production server:

```
npm start
```

## Available Scripts

- `npm run dev`: Runs the app in development mode
- `npm run build`: Builds the app for production
- `npm start`: Starts the production server
- `npm run lint`: Runs the linter
- `npm run format`: Formats the code using Prettier

## Project Structure

- `/app`: Contains the Next.js 13 app router pages and layouts
- `/components`: Reusable React components
- `/lib`: Utility functions and shared code
- `/prisma`: Prisma schema and migrations
- `/public`: Static assets

## Technologies Used

- Next.js 13
- React
- TypeScript
- Prisma
- Tailwind CSS
- PostgreSQL

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
