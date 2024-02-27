import "./App.css";
import useFetch from "./hooks/useFetch";

function App() {
  const { loading, data, error } = useFetch<{
    posts: { id: number; title: string; content: string }[];
  }>("/api/posts");

  return (
    <main>
      <h1>React - Vite / Django</h1>
      {loading && <p>Wait for the Fake api to load ... </p>}
      {error && <p data-error>{error}</p>}
      {data?.posts.map((post) => (
        <div key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
        </div>
      ))}
    </main>
  );
}

export default App;
