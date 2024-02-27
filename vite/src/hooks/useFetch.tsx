import { useState, useEffect } from "react";
import sleep from "../utils/sleep";

export default function useFetch<T>(url: string) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [data, setData] = useState<T | null>(null);

  useEffect(() => {
    (async () => {
      setLoading(true);
      await sleep(1000);
      const res = await fetch(url);
      const data = await res.json().catch((error) => {
        console.error(error);
        setError(error.message);
        setLoading(false);
      });
      if (!data) {
        setError("error fetching data");
        setLoading(false);
        return;
      }
      setData(data);
      setLoading(false);
    })();
  }, [url]);

  return { loading, error, data };
}
