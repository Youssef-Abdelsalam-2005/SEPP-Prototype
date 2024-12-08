document.getElementById("fetch-data").addEventListener("click", function () {
  fetch("http://localhost:5000/api/data")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("data").innerText = data.message;
    })
    .catch((error) => console.error("Error fetching data:", error));
});

const getCarts = async () => {
  try {
    const response = await fetch("http://localhost:5000/carts", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const createCart = async (building_id) => {
  try {
    const response = await fetch("http://localhost:5000/carts/create", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ building_id }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const getCart = async (cart_id) => {
  try {
    const response = await fetch(`http://localhost:5000/carts/${cart_id}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const addToCart = async (cart_id, item_id, username) => {
  try {
    const response = await fetch(
      `http://localhost:5000/carts/${cart_id}/add/${item_id}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username }),
      }
    );

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const removeFromCart = async (cart_id, item_id, username) => {
  try {
    const response = await fetch(
      `http://localhost:5000/carts/${cart_id}/remove/${item_id}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username }),
      }
    );

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};
