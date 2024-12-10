from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, timedelta

router = APIRouter()

# Modelos de datos
class CrearCitaRequest(BaseModel):
    fecha_inicio: str = Field(..., pattern=r"\d{4}-\d{2}-\d{2}")
    hora_inicio: str = Field(..., pattern=r"\d{2}:\d{2}")
    nombre_paciente: str
    celular_contacto: str
    motivo_consulta: str

class EditarCitaRequest(BaseModel):
    id_cita: str
    nueva_fecha: str
    nuevo_horario: str

class BuscarCitaRequest(BaseModel):
    nombre_paciente: str
    celular_contacto: str

class BorrarCitaRequest(BaseModel):
    id_cita: str

# Endpoints
@router.post("/crear_cita")
async def crear_cita(data: CrearCitaRequest):
    try:
        # Cálculo de fecha y hora final
        fecha_inicio = data.fecha_inicio
        hora_inicio = datetime.strptime(data.hora_inicio, "%H:%M")
        hora_fin = (hora_inicio + timedelta(minutes=45)).strftime("%H:%M")
        fecha_fin = fecha_inicio

        # Crear la respuesta para Make
        response = {
            "fecha_inicio": fecha_inicio,
            "hora_inicio": data.hora_inicio,
            "fecha_fin": fecha_fin,
            "hora_fin": hora_fin,
            "nombre_paciente": data.nombre_paciente,
            "celular_contacto": data.celular_contacto,
            "motivo_consulta": data.motivo_consulta,
        }

        return {"mensaje": "Datos calculados correctamente", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear la cita: {e}")

@router.post("/buscar_cita")
async def buscar_cita(data: BuscarCitaRequest):
    try:
        # Simulación de respuesta desde Make (reemplazar con conexión real)
        response = {
            "mensaje": "Cita encontrada",
            "id": "cita123456",  # Ejemplo de ID
            "fecha_inicio": "2024-01-01",
            "hora_inicio": "10:00",
            "hora_fin": "10:45",
            "nombre_paciente": data.nombre_paciente,
            "celular_contacto": data.celular_contacto,
            "motivo_consulta": "Consulta de rutina"
        }

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar la cita: {e}")

@router.put("/editar_cita")
async def editar_cita(data: EditarCitaRequest):
    try:
        # Simular consulta de la cita original (esto debería venir de una base de datos en un entorno real)
        cita_original = {
            "id_cita": data.id_cita,
            "nombre_paciente": "Juan Pérez",
            "celular_contacto": "1234567890",
            "motivo_consulta": "Consulta general"
        }

        # Cálculo de la nueva hora final
        nuevo_horario_inicio = datetime.strptime(data.nuevo_horario, "%H:%M")
        nuevo_horario_final = (nuevo_horario_inicio + timedelta(minutes=45)).strftime("%H:%M")

        # Combinar datos originales con los nuevos
        response = {
            "id_cita": cita_original["id_cita"],
            "nombre_paciente": cita_original["nombre_paciente"],
            "celular_contacto": cita_original["celular_contacto"],
            "motivo_consulta": cita_original["motivo_consulta"],
            "nueva_fecha_inicio": data.nueva_fecha,
            "nuevo_horario_inicio": data.nuevo_horario,
            "nuevo_horario_final": nuevo_horario_final,
            "event_id": "test-event-id-123"  # Este debería ser el ID real del evento en Google Calendar
        }

        return {"mensaje": "Datos de edición calculados correctamente", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al editar la cita: {e}")


@router.delete("/borrar_cita")
async def borrar_cita(data: BorrarCitaRequest):
    try:
        # Crear la respuesta para Make
        response = {
            "id_cita": data.id_cita,
        }

        return {"mensaje": "Cita eliminada correctamente", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al borrar la cita: {e}")
